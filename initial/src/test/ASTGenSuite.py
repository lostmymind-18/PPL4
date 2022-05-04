import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_simple_program1(self):
        """start1"""
        input="""
        Class Shape{
            $count(y : Int){
                Return y;
            }
        }
        Class Program{
            Val y : Int = 10;
            Val sh: Shape = New Shape();
            Var x : Int = Shape::$count(Self.sh.x);
        }
        """
        expect = "Program([ClassDecl(Id(Program),[])])"
        self.assertTrue(TestAST.test(input,expect,301))