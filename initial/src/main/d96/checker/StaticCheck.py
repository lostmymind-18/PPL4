#1912966
from AST import * 
from Visitor import *
from StaticError import *

class MType:
    def __init__(self,partype,rettype):
        self.partype = partype
        self.rettype = rettype

class Symbol:
    def __init__(self,name,mtype,value = None):
        self.name = name
        self.mtype = mtype
        self.value = value

class StaticChecker(BaseVisitor):

    global_envi = [
    Symbol("getInt",MType([],IntType())),
    Symbol("putIntLn",MType([IntType()],VoidType()))
    ]
            
    
    def __init__(self,ast):
        self.ast = ast

 
    
    def check(self):
        return self.visit(self.ast,StaticChecker.global_envi)

    def visitProgram(self,ast, c):
        env = [{}] 
        for cls in ast.decl:
            self.visit(cls,env)
    
    def visitClassDecl(self,ast,c):
        id = ast.classname.name
        if id in c[0]:
            raise Redeclared(Class(),id)
        #Check if Superclass's declared or not
        if ast.parentname != None:
            if ast.parentname.name not in c[len(c)-1]:
                raise Undeclared(Class(),ast.parentname.name)
             
        env = [{}] + c
        c[0][id] = env[0]
        for mem in ast.memlist:
            self.visit(mem,env)
            
    def visitAttributeDecl(self,ast,c):
        if str(type(ast.decl)) == '<class \'AST.VarDecl\'>':
            id = ast.decl.variable.name
            if id in c[0]:
                raise Redeclared(Attribute(),id)
            
        elif str(type(ast.decl)) == '<class \'AST.ConstDecl\'>':
            id = ast.decl.constant.name
            if id in c[0]:
                raise Redeclared(Attribute(),id)
            
        self.visit(ast.decl,c)
        
    
    def visitVarDecl(self,ast,c):
        id = ast.variable.name
        #if this variable in a parameter declared
        if 'paras' in c[0] and id in c[0]:
            raise Redeclared(Parameter(),id)
        #if this variable in a function that we should check the parameters
            #of that function
        if 'function' in c[0]:
            if id in c[0] or id in c[0]['function']:
                raise Redeclared(Variable(),id)
            
        elif 'for' in c[0]:
            if id in c[0] or id in c[0]['for']:
                raise Redeclared(Variable(),id)
        
        else:
            if id in c[0]:
                raise Redeclared(Variable(),id)
        #if initial value of a variable is a Id, visit that Id to see
            #if it's declared or not
        if ast.varInit != None:
            self.visit(ast.varInit,c)
        #Check varType oke or not(class type exist or not)    
        c[0][id] = self.visit(ast.varType,c)
        
    def visitConstDecl(self,ast,c):
        id = ast.constant.name
        if 'function' in c[0]:
            if id in c[0] or id in c[0]['function']:
                raise Redeclared(Constant(),id)
        elif 'for' in c[0]:
            if id in c[0] or id in c[0]['for']:
                raise Redeclared(Constant(),id)
        else:
            if id in c[0]:
                raise Redeclared(Constant(),id)
        if ast.value != None:
            self.visit(ast.value,c)
        #check consttype oke or not(class type exist or not)
        c[0][id] = self.visit(ast.constType,c)
        
        
    def visitMethodDecl(self,ast,c):
        id = ast.name.name
        if id in c[0]:
            raise Redeclared(Method(),ast.name.name)
        #TODO later
        paras = [{}]
        paras[0]['paras'] = True
        for decl in ast.param:
            self.visit(decl,paras)    
        c[0][id] = paras
        env = [('function',paras[0])] + c
        self.visit(ast.body,env)

        
    def visitBlock(self,ast,c):
        env = None
        #If block belong to a function
        if type(c[0]) == tuple and c[0][0] == 'function':
            paras = c[0][1]
            c[0] = {}
            c[0]['function'] = paras
            env = c
            
        elif type(c[0]) == tuple and c[0][0] == 'for':
            scalar = c[0][1]
            c[0] = {}
            c[0]['for'] = scalar
            env = c
        
        else:
            env = [{}] + c
        for inst in ast.inst:
            self.visit(inst,env)
            
    def visitId(self,ast,c):
        a = False
            
        if 'function' in c[0] and ast.name in c[0]['function']:
            a = True
            
        if 'for' in c[0] and ast.name in c[0]['for']:
            a = True  
            
        if a == False:        
            for cx in c[:-2]:
                if ast.name in cx:
                    a = True
                    break
              
        
        if a == False:
            raise Undeclared(Identifier(),ast.name)
        ttype = None
        return self.getType(ast.name,c)
    
    def visitClassType(self,ast,c):
        #Check undeclared class
        if ast.classname not in c[len(c) - 1]:
            raise Undeclared(Class(),ast.classname)
        return ast.classname
    
    def visitNewExpr(self,ast,c):
        if ast.classname not in c[len(c) - 1]:
            raise Undeclared(Class(),ast.classname)
        for para in ast.param:
            self.visit(para,c)
        
    def visitFieldAccess(self,ast,c):
        #Static access
        if ast.fieldname.name[0] == '$':
            if ast.obj.name not in c[len(c) - 1]:
                raise Undeclared(Class(),ast.obj.name)
            if ast.fieldname.name not in c[len(c)-1][ast.obj.name]:
                raise Undeclared(Attribute(),ast.fieldname.name)
            else:
                return c[len(c) - 1][ast.obj.name][ast.field.name]
        #Instance access
        else:
            #Check obj id
            objtype = self.visit(ast.obj,c)
            if objtype in c[len(c) - 1]:
                if ast.fieldname.name not in c[len(c) - 1][objtype]:
                    raise Undeclared(Attribute(),ast.fieldname.name)
                return c[len(c) - 1][objtype][ast.fieldname.name]
            if objtype == 'Self':
                if ast.fieldname.name not in c[len(c) - 2]:
                    raise Undeclared(Attribute(),ast.fieldname.name)
                return c[len(c) - 2][ast.fieldname.name]    
            #TODO    

            
    
    def visitArrayCell(self,ast,c):
        self.visit(ast.arr,c)
        for idx_ in ast.idx:
            self.visit(idx_,c)
        
        
    def visitCallExpr(self,ast,c):
        #Static
        if ast.method.name[0] == '$':
            if ast.obj.name not in c[len(c) - 1]:
                raise Undeclared(Class(),ast.obj.name)
            if ast.method.name not in c[len(c) - 1][ast.obj.name]:
                raise Undeclared(Method(),ast.method.name)
            else:
                for para in ast.param:
                    self.visit(para,c)
                return c[len(c) - 1][ast.obj.name][ast.method.name]
            
        #Instance
        else:
            objtype = self.visit(ast.obj,c)
            if objtype in c[len(c) - 1]:
                if ast.method.name not in c[len(c) - 1][objtype]:
                    raise Undeclared(Method(),ast.method.name)
                for para in ast.param:
                    self.visit(para,c)
                return c[len(c) - 1][objtype][ast.method.name]

            if objtype == 'Self':
                if ast.method.name not in c[len(c) - 2]:
                    raise Undeclared(Method(),ast.method.name)
                for para in ast.param:
                    self.visit(para,c)
                return c[len(c) - 2][ast.method.name]
            
    
    
    def visitBinaryOp(self,ast,c):
        self.visit(ast.left,c)
        self.visit(ast.right,c)
        

    def visitUnaryOp(self,ast,c):
        self.visit(ast.body,c)
    
    
    
    
    def visitArrayType(self,ast,c):pass
    
        
    def visitFloatType(self,ast,c): pass


    def visitStringType(self,ast,c):pass    
    
    
    
    def visitIntLiteral(self,ast,c): pass
    
    
    def visitFloatLiteral(self,ast,c): pass
    
    
    def visitStringLiteral(self,ast,c):pass
    
    
    def visitArrayLiteral(self,ast,c):
        for val in ast.value:
            self.visit(val,c)


    def visitSelfLiteral(self,ast,c):
        return 'Self'
    

    def visitAssign(self,ast,c):
        self.visit(ast.lhs,c)
        self.visit(ast.exp,c)
        
    
    def visitIf(self,ast,c):
        self.visit(ast.expr,c)
        self.visit(ast.thenStmt,c)
        self.visit(ast.elseStmt,c)
        
    
    def visitFor(self,ast,c):
        env = [('for',{ast.id.name:'Int'})] + c
        self.visit(ast.expr1,c)
        self.visit(ast.expr2,c)
        self.visit(ast.expr3,c)
        self.visit(ast.loop,env)
        
        
    def visitReturn(self,ast,c):
        if ast.expr != None:
            self.visit(ast.expr,c)

            
    def visitCallStmt(self,ast,c):
        #If method is a static
        if ast.method.name[0] == '$':
            classname = ast.obj.name
            if classname not in c[len(c)-1]:
                raise Undeclared(Class(),classname)
        else:
            self.visit(ast.obj,c)
        for para in ast.param:
            self.visit(para,c)
            
            
    def getType(self,id,c):
        for cx in c:
            if id in cx:
                return cx[id]
            if 'function' in cx and id in cx['function']:
                return cx['function'][id]
            if 'for' in cx and id in cx['for']:
                return cx['for'][id]     
            
        return None