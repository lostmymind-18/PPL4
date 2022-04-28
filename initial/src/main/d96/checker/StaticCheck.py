
"""
 * @author nhphung
"""
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
        for cls in ast.decl:
            self.visit(cls,c)
    
    def visitClassDecl(self,ast,c):
        o = [{}]
        for mem in ast.memlist:
            self.visit(mem,o)
            
    def visitAttributeDecl(self,ast,c):
        self.visit(ast.decl,c)
        
    def visitVarDecl(self,ast,c):
        if ast.variable.name in c[0]:
            raise Redeclared(Variable,ast.variable.name)
        c[0][ast.variable.name] = [ast.varType,ast.varInit.value]
        
    def visitConstDecl(self,ast,c):
        if ast.constant.name in c[0]:
            raise Redeclared(Constant,ast.constant.name)
        c[0][ast.constant.name] = [ast.constType,ast.value.vale]
        
    
        

    

