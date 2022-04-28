import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):
    def test_undeclared_function(self):
        """Simple program: int main() {} """
        input="""Class Rectangle {
            Var x: Int = 10;
            Val x: Int = 10;
        }"""
        expect = "Redeclared(Constant,x)"
        self.assertTrue(TestChecker.test(input,expect,401))