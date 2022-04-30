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
        c[0][id] = 'class'
        env = [{}] + c
        for mem in ast.memlist:
            self.visit(mem,env)
            
    def visitAttributeDecl(self,ast,c):
        if str(type(ast.decl)) == '<class \'AST.VarDecl\'>':
            id = ast.decl.variable.name
            if id in c[0]:
                raise Redeclared(Attribute(),id)
            
            #if initial value of attribute is a Id, visit that Id to see
                #if it's declared or not
            self.visit(ast.decl.varInit,c)
            c[0][id] = str(ast.decl.varType)
        
        elif str(type(ast.decl)) == '<class \'AST.ConstDecl\'>':
            id = ast.decl.constant.name
            if id in c[0]:
                raise Redeclared(Attribute(),id)
            c[0][id] = str(ast.decl.constType)
        
    def visitMethodDecl(self,ast,c):
        id = ast.name.name
        if id in c[0]:
            raise Redeclared(Method(),ast.name.name)
        #TODO later
        c[0][id] = 'method'
        paras = [{}]
        for decl in ast.param:
            self.visit(decl,paras)    
        env = [({},paras[0])] + c
        for inst in ast.body.inst:
            self.visit(inst,env)
    
    def visitVarDecl(self,ast,c):
        id = ast.variable.name
        #if this variable in a function that we should check the parameters
            #of that function
        if type(c[0]) == tuple:
            if id in c[0][0] or id in c[0][1]:
                raise Redeclared(Variable(),id)
        else:
            if id in c[0]:
                raise Redeclared(Variable(),id)
        #if initial value of a variable is a Id, visit that Id to see
            #if it's declared or not
        if ast.varInit != None:
            self.visit(ast.varInit,c)
        if type(c[0]) == tuple:
            c[0][0][id] = str(ast.varType)
        else:
            c[0][id] = str(ast.varType)
        
    def visitConstDecl(self,ast,c):
        id = ast.constant.name
        if type(c[0]) == tuple:
            if id in c[0][0] or id in c[0][1]:
                raise Redeclared(Constant(),id)
        else:
            if id in c[0]:
                raise Redeclared(Constant(),id)
        if ast.value != None:
            self.visit(ast.value,c)
        if type(c[0]) == tuple:
            c[0][0][id] = str(ast.constType)
        else:
            c[0][id] = str(ast.constType)
        
    def visitBlock(self,ast,c):
        env = None
        #If block belong to a function
        if type(c[0]) == tuple:
            env = c
        else:
            env = [{}] + c
        for inst in ast.inst:
            self.visit(inst,env)
            
    def visitId(self,ast,c):
        a = False
        for cx in c:
            if ast.name in cx:
                a = True
                break
        if a == False:
            raise Undeclared(Identifier(),ast.name)
        return ast.name
                
        
    
        

    

