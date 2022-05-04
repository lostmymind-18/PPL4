import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):
        
    #---TEST REDECLARED---#
    def test_redeclared1(self):
        """Test redeclared"""
        input="""Class Rectangle {
            Var x: Int = 10;
            Val x: Int = 10;
        }"""
        expect = "Redeclared Attribute: x"
        self.assertTrue(TestChecker.test(input,expect,401))
        

    def test_redeclared2(self):
        """Test redeclared"""
        input="""Class Rectangle {
            Var $x: Int = 10;
            Val $x: Int = 10;
        }"""
        expect = "Redeclared Attribute: $x"
        self.assertTrue(TestChecker.test(input,expect,402))
                

    def test_redeclared3(self):
        """Test redeclared"""
        input="""Class Rectangle {
            Var $x: Int = 10;
            Var $x: Int = 10;
        }"""
        expect = "Redeclared Attribute: $x"
        self.assertTrue(TestChecker.test(input,expect,403))
        
    
    def test_redeclared4(self):
        """Test redeclared"""
        input="""Class Rectangle {
            Var $x: Int = 10;
            $x(){}
        }"""
        expect = "Redeclared Method: $x"
        self.assertTrue(TestChecker.test(input,expect,404))      
        
        
    def test_redeclared5(self):
        """Test redeclared"""
        input="""Class Rectangle {
            $x(a,b:Int;c,a:Int){}
        }"""
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input,expect,405))
        
        
    def test_redeclared6(self):
        """Test redeclared"""
        input="""Class Rectangle {
            $x(a,b:Int;c,d:Int){
                Var x: Int = 10;
                Val x: Int = 20;
            }
        }"""
        expect = "Redeclared Constant: x"
        self.assertTrue(TestChecker.test(input,expect,406))
        
        
    def test_redeclared7(self):
        """Test redeclared"""
        input="""Class Rectangle {
            $x(a,b:Int;c,d:Int){
                Val y: Int = 10;
                Var y: Int = 20;
            }
        }"""
        expect = "Redeclared Variable: y"
        self.assertTrue(TestChecker.test(input,expect,407))                          
        

    def test_redeclared8(self):
        """Test redeclared"""
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
        
        
    def test_redeclared9(self):
        """Test redeclared"""
        input="""Class Rectangle {
            method1(a,b:Int;c,d:Int){
                Var x: Int = 10;
                {
                    Val x: Float = 10.2;
                    Var y: Int = 10;
                    Val z: Int = 10;
                    Val b: Int = 20;
                }
            }
            method1(a,b:Int;c,d:Int){
                Var x: Int = 10;
                {
                    Val x: Float = 10.2;
                    Var y: Int = 10;
                    Val z: Int = 10;
                    Val b: Int = 20;
                }
            }
        }"""
        expect = "Redeclared Method: method1"
        self.assertTrue(TestChecker.test(input,expect,409))
        
        
    def test_redeclared10(self):
        """Test redeclared"""
        input="""Class Rectangle {
            method1(a,b:Int;c,d:Int){
                Var x: Int = 10;
                {
                    Val x: Float = 10.2;
                    Var y: Int = 10;
                    Val z: Int = 10;
                    Val b: Int = 20;
                }
            }
            method2(a,b:Int;c,d:Int){
                Var x: Int = 10;
                {
                    Val x: Float = 10.2;
                    Var y: Int = 10;
                    Val z: Int = 10;
                    Val b: Int = 20;
                }
            }
        }
        Class Rectangle {
            method1(a,b:Int;c,d:Int){
                Var x: Int = 10;
                {
                    Val x: Float = 10.2;
                    Var y: Int = 10;
                    Val z: Int = 10;
                    Val b: Int = 20;
                }
            }
            method2(a,b:Int;c,d:Int){
                Var x: Int = 10;
                {
                    Val x: Float = 10.2;
                    Var y: Int = 10;
                    Val z: Int = 10;
                    Val b: Int = 20;
                }
            }
        }"""
        expect = "Redeclared Class: Rectangle"
        self.assertTrue(TestChecker.test(input,expect,410))
        

        
    #---TEST UNDECLARED---#           
    def test_undeclared1(self):
        """Test undeclared identifier"""
        input="""Class Rectangle {
            Var x: Int = y;
        }"""
        expect = "Undeclared Identifier: y"
        self.assertTrue(TestChecker.test(input,expect,411))
        
        
    def test_undeclared2(self):
        """Test undeclared identifier"""
        input="""Class Rectangle {
            Var x: Int = 10;
            Val y: Int = Self.x;
            a(){
                Var z : Float = Self.x;
                Var f : Float = z;
                Var y : Float = m;
            }
        }"""
        expect = "Undeclared Identifier: m"
        self.assertTrue(TestChecker.test(input,expect,412))
        
        
    def test_undeclare3(self):
        """Test undeclared identifier"""
        input="""Class Rectangle {
            Var x: Int = 10;
            Val y: Int = Self.x;
            a(){
                Var z : Float = Self.x;
                Var f : Float = z;
            }
            Val $x : Int = z;
        }"""
        expect = "Undeclared Identifier: z"
        self.assertTrue(TestChecker.test(input,expect,413))
        
        
    def test_undeclare4(self):
        """Test undeclared identifier"""
        input="""Class Rectangle {
            Var x: Int = 10;
            Val y: Int = Self.x;
            a(){
                Var z : Float = Self.x;
                Var f : Float = z;
            }
            Val $x : Int = Self.z;
        }"""
        expect = "Undeclared Attribute: z"
        self.assertTrue(TestChecker.test(input,expect,414))
        

    def test_undeclare5(self):
        """Test undeclared identifier"""
        input="""Class Rectangle {
            Var x: Int = 10;
            Val y: Int = Self.x;
            a(){
                Var z : Float = Self.x;
                Var f : Float = z;
            }
            Val $x : Int = z;
        }"""
        expect = "Undeclared Identifier: z"
        self.assertTrue(TestChecker.test(input,expect,415))
        
        
    def test_undeclare6(self):
        """Test undeclared identifier"""
        input="""
        Class Shape{
            $count(y : Int){
                Return y;
            }
        }
        Class Program{
            Val y : Int = 10;
            Var x : Int = Shape::$count(Self.y);
            Method(){
                Val y : Int = Shape::$count(z);
            }
        }
        """
        expect = "Undeclared Identifier: z"
        self.assertTrue(TestChecker.test(input,expect,416))        
        
        
    def test_undeclare7(self):
        """Test undeclared identifier"""
        input="""
        Class Shape{
            Var x: Int = 5 + $y;
            $count(y : Int){
                Return y;
            }
        }
        """
        expect = "Undeclared Identifier: $y"
        self.assertTrue(TestChecker.test(input,expect,417))
        
        
    def test_undeclare8(self):
        """Test undeclared identifier"""
        input="""
        Class Shape{
            Var x: Int = -(3+5);
            Val y: Int = -z;
            $count(y : Int){
                Return y;
            }
        }
        """
        expect = "Undeclared Identifier: z"
        self.assertTrue(TestChecker.test(input,expect,418))
        
        
    def test_undeclare9(self):
        """Test undeclared identifier"""
        input="""
        Class Rectangle{
            size(){}
        }
        Class Shape{
            Var x: Int = -(3+5);
            Val y: Int = -Self.x;
            $count(y : Int){
                Var z: Int = rec.size();
            }
        }
        """
        expect = "Undeclared Identifier: rec"
        self.assertTrue(TestChecker.test(input,expect,419))
        
        
    def test_undeclare10(self):
        """Test undeclared identifier"""
        input="""
        Class Rectangle{
            size(x,y:Int){}
        }
        Class Shape{
            Var x: Int = -(3+5);
            Val y: Int = -Self.x;
            Val rec: Rectangle = New Rectangle();
            $count(y : Int){
                Var z: Int = Self.rec.size(y,z);
            }
        }
        """
        expect = "Undeclared Identifier: z"
        self.assertTrue(TestChecker.test(input,expect,420))
        
        
    def test_undeclare11(self):
        """Test undeclared identifier"""
        input="""
        Class Rectangle{
            size(x,y:Int){}
        }
        Class Shape{
            Var x: Int = -(3+5);
            Val y: Int = -Self.x;
            Val rec: Rectangle = New Rectangle(Self.x,z);
        }
        """
        expect = "Undeclared Identifier: z"
        self.assertTrue(TestChecker.test(input,expect,421))        
        
        
    def test_undeclare12(self):
        """Test undeclared identifier"""
        input="""
        Class Rectangle{
            size(x,y:Int){}
        }
        Class Shape{
            Var x: Int = -(3+5);
            Val y: Int = -Self.x;
            Val rec: Rectangle = New Rectangle(Self.x,Self.y);
            Val arr: Array[String,3] = Array("abc","xyz","aaa");
            Method(){
                Var z:Int = arr[k];
            }
        }
        """
        expect = "Undeclared Identifier: arr"
        self.assertTrue(TestChecker.test(input,expect,422))
        
        
    def test_undeclare13(self):
        """Test undeclared identifier"""
        input="""
        Class Rectangle{
            size(x,y:Int){}
        }
        Class Shape{
            Var x: Int = -(3+5);
            Val y: Int = -Self.x;
            Val rec: Rectangle = New Rectangle(Self.x,Self.y);
            Val arr: Array[String,3] = Array("abc","xyz","aaa");
            Method(){
                Var z:Int = Self.arr[k];
            }
        }
        """
        expect = "Undeclared Identifier: k"
        self.assertTrue(TestChecker.test(input,expect,423))
        
        
    def test_undeclare14(self):
        """Test undeclared identifier"""
        input="""
        Class Rectangle{
            size(x,y:Int){}
        }
        Class Shape{
            Var x: Int = -(3+5);
            Val y: Int = rec.size();
            Val rec: Rectangle = New Rectangle(x,y);
            Val arr: Array[String,3] = Array("abc","xyz","aaa");
            Method(){
                Var z:Int = Self.arr[k];
            }
        }
        """
        expect = "Undeclared Identifier: rec"
        self.assertTrue(TestChecker.test(input,expect,424))
        
        
    def test_undeclare15(self):
        """Test undeclared identifier"""
        input="""
        Class Rectangle{
            size(x,y:Int){}
        }
        Class Shape{
            Var x: Int = -(3+5);
            Var y: String = "xyz";
            Val rec: Rectangle = New Rectangle(Self.x,Self.y);
            Val arr: Array[String,3] = Array("abc",Self.y,k);
        }
        """
        expect = "Undeclared Identifier: k"
        self.assertTrue(TestChecker.test(input,expect,425))
                
        
    def test_undeclare16(self):
        """Test undeclared identifier"""
        input="""
        Class Rectangle{
            size(x,y:Int){}
        }
        Class Shape{
            Var x: Int = -(3+5);
            Var y: String = "xyz";
            Method()
            {
                Var x: Int = 5;
                Var z: Int;
                z = k;    
            }
        }
        """
        expect = "Undeclared Identifier: k"
        self.assertTrue(TestChecker.test(input,expect,426))
        
        
    def test_undeclare17(self):
        """Test undeclared identifier"""
        input="""
        Class Rectangle{
            size(x,y:Int){}
        }
        Class Shape{
            Var x: Int = -(3+5);
            Var y: String = "xyz";
            Method()
            {
                Var x: Int = 5;
                Var z: Int;
                If(k > 3)
                {
                    z = 7;
                }
            }
        }
        """
        expect = "Undeclared Identifier: k"
        self.assertTrue(TestChecker.test(input,expect,427))
        
        
        
    def test_undeclare18(self):
        """Test undeclared identifier"""
        input="""
        Class Rectangle{
            size(x,y:Int){}
        }
        Class Shape{
            Var x: Int = -(3+5);
            Var y: String = "xyz";
            Method()
            {
                Var x: Int = 5;
                Var z: Int;
                If(x > 3)
                {
                    z = 7;
                }
                Elseif(k < 3)
                {
                    z = 55;
                }
            }
        }
        """
        expect = "Undeclared Identifier: k"
        self.assertTrue(TestChecker.test(input,expect,428))
        
        
        
    def test_undeclare19(self):
        """Test undeclared identifier"""
        input="""
        Class Rectangle{
            size(x,y:Int){}
        }
        Class Shape{
            Var x: Int = -(3+5);
            Var y: String = "xyz";
            Method()
            {
                Foreach(i In 1 .. 100 By 2){
                    i = A[i];
                }
            }
        }
        """
        expect = "Undeclared Identifier: A"
        self.assertTrue(TestChecker.test(input,expect,429))
        
        
    def test_undeclare20(self):
        """Test undeclared identifier"""
        input="""
        Class Rectangle{
            size(x,y:Int){}
        }
        Class Shape{
            Var x: Int = -(3+5);
            Var y: String = "xyz";
            Method()
            {
                Val z: Int = 100;
                Foreach(i In z .. u By 2){
                    i = A[i];
                }
            }
        }
        """
        expect = "Undeclared Identifier: u"
        self.assertTrue(TestChecker.test(input,expect,430))
        
        
    def test_undeclare21(self):
        """Test undeclared class"""
        input="""
        Class Abc{
            Constructor(x:Int){}
        }
        Class Rectangle {
            Var x: Int = 10;
            Val y: Abc = New Abc(Self.x);
            Method(){
                Return z;
            }
        }"""
        expect = "Undeclared Identifier: z"
        self.assertTrue(TestChecker.test(input,expect,431))   
        
        
    def test_undeclare22(self):
        """Test undeclared class"""
        input="""
        Class Abc{
            Constructor(x:Int){}
            Size(x,y:Int){}
        }
        Class Rectangle {
            Var x: Int = 10;
            Val y: Abc = New Abc(Self.x);
            Method(){
                Var z: Int = 10;
                Self.y.Size(z,k);
            }
        }"""
        expect = "Undeclared Identifier: k"
        self.assertTrue(TestChecker.test(input,expect,432))     
        
        
    def test_undeclare23(self):
        """Test undeclared class"""
        input="""Class Rectangle {
            Var x: Int = 10;
            Val y: Abc = New Abc(x);
        }"""
        expect = "Undeclared Class: Abc"
        self.assertTrue(TestChecker.test(input,expect,433))
        
        
    def test_undeclare24(self):
        """Test undeclared class"""
        input="""Class Rectangle {
            Var x: Int = 10;
            Val y: Abc = New Rectangle(Self.x);
        }"""
        expect = "Undeclared Class: Abc"
        self.assertTrue(TestChecker.test(input,expect,434))
        
        
    def test_undeclare25(self):
        """Test undeclared class"""
        input="""Class Rectangle {
            Var x: Int = 10;
            Val y: Rectangle = New Rectangle(Self.x);
        }
                Class Shape:Rectangle{
            
        }
            Class Abc:Xyz{}
        """
        expect = "Undeclared Class: Xyz"
        self.assertTrue(TestChecker.test(input,expect,435))
        

    def test_undeclare26(self):
        """Test undeclared class"""
        input="""
        Class Program{
            Var x : Int = Shape::$x;
        }
        """
        expect = "Undeclared Class: Shape"
        self.assertTrue(TestChecker.test(input,expect,436))
        

    def test_undeclare27(self):
        """Test undeclared class"""
        input="""
        Class Program{
            Val y : Int = 10;
            Var x : Int = Shape::$count(y);
        }
        """
        expect = "Undeclared Class: Shape"
        self.assertTrue(TestChecker.test(input,expect,437))
        
    
    def test_undeclare28(self):
        """Test undeclared class"""
        input="""
        Class Shape{
            $count(y : Int){
                Return y;
            }
        }
        Class Program{
            Val y : Int = 10;
            Var x : Int = Shape::$count(Self.y);
            Method(){
                Val y : Int = Shape::$count(Self.x);
                Val z : Int = Shoo::$abc;
            }
        }
        """
        expect = "Undeclared Class: Shoo"
        self.assertTrue(TestChecker.test(input,expect,438))
        
        
    def test_undeclare29(self):
        """Test undeclared class"""
        input="""
        Class Shape{
            $count(y : Int){
                Return y;
            }
        }
        Class Program{
            Val y : Int = 10;
            Var x : Int = Shape::$count(Self.y);
            Method(){
                Val y : Int = Shape::$count(Self.x);
                Shoo::$take();
            }
        }
        """
        expect = "Undeclared Class: Shoo"
        self.assertTrue(TestChecker.test(input,expect,439))

        
    def test_undeclare30(self):
        """Test undeclared attribute"""
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
        expect = "Undeclared Attribute: x"
        self.assertTrue(TestChecker.test(input,expect,440))
        


    def test_undeclare31(self):
        """Test undeclared attribute"""
        input="""
        Class Shape{
            $count(y : Int){
                Return y;
            }
        }
        Class Program{
            Val y : Int = 10;
            Val sh: Shape = New Shape();
            Var x : Int = Shape::$count(Self.x);
        }
        """
        expect = "Undeclared Attribute: x"
        self.assertTrue(TestChecker.test(input,expect,441))
        
        
    def test_undeclare32(self):
        """Test undeclared attribute"""
        input="""
        Class Shape{
            Val z: Int = 10;
            $count(y : Int){
                Return Self.z;
            }
        }
        Class Program{
            Val sh: Shape = New Shape();
            Var x : Int = Shape::$count(Self.sh.z);
            Val y : Int = Self.sh.u;
        }
        """
        expect = "Undeclared Attribute: u"
        self.assertTrue(TestChecker.test(input,expect,442))
        
        
    def test_undeclare33(self):
        """Test undeclared method"""
        input="""
        Class Shape{
            Val z: Int = 10;
            $count(y : Int){
                Return Self.z;
            }
        }
        Class Program{
            Val sh: Shape = New Shape();
            Var x : Int = Shape::$count(Self.sh.z);
            Val y : Int = Self.sh.size();
        }
        """
        expect = "Undeclared Method: size"
        self.assertTrue(TestChecker.test(input,expect,443))
        
        
    def test_undeclare34(self):
        """Test undeclared method"""
        input="""
        Class Shape{
            Val z: Int = 10;
            $count(y : Int){
                Return Self.z;
            }
        }
        Class Program{
            Val sh: Shape = New Shape();
            Var x : Int = Shape::$count(Self.sh.z);
            Val y : Int = Self.sh.size();
        }
        """
        expect = "Undeclared Method: size"
        self.assertTrue(TestChecker.test(input,expect,444))
        
        
    