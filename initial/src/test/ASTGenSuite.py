import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_simple_program1(self):
        """start1"""
        input="""Class Rectangle {
            Var x: Int = 10;
            Val y: Int = x;
            a(){
                Var z : Float = x;
                Var f : Float = z;
                Var y : Float = m;
            }
        }"""
        expect = "Program([ClassDecl(Id(Program),[])])"
        self.assertTrue(TestAST.test(input,expect,301))