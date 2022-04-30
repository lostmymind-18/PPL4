import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):
    #---TEST REDECLARED---#
        
    def test_redeclared8(self):
        """Simple program: int main() {} """
        input="""Class Rectangle {
            $x(a,b:Int;c,d:Int){
                Var x: Int = 10;
                {
                    Val x: Float = 10.2;
                    Var y: Int = 10;
                    Val z: Int = 10;
                    Val y: Int = 20;
                }
            }
        }"""
        expect = "Redeclared Constant: y"
        self.assertTrue(TestChecker.test(input,expect,408))
        

        
    