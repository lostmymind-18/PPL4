from AST import *
from D96Visitor import D96Visitor
from D96Parser import D96Parser


class ASTGeneration(D96Visitor):
    def visitProgram(self, ctx: D96Parser.ProgramContext):
        return Program(self.visit(ctx.list_class()))
        
        
    def visitList_class(self,ctx: D96Parser.List_classContext):
        if ctx.getChildCount()>1:
            return [self.visit(ctx.class_decl())]+self.visit(ctx.list_class())
        
        return [self.visit(ctx.class_decl())]
        
    def visitClass_decl(self, ctx: D96Parser.Class_declContext):
        if ctx.COLON():
            return ClassDecl(Id(ctx.ID(0).getText()),self.visit(ctx.class_block()),Id(ctx.ID(1).getText()))
        return ClassDecl(Id(ctx.ID(0).getText()),self.visit(ctx.class_block()))
        
        
    def visitClass_block(self, ctx: D96Parser.Class_blockContext):
        if ctx.getChildCount()>0:
            return self.visit(ctx.list_class_mem())
        return []
        
        
    def visitList_class_mem(self, ctx: D96Parser.List_class_memContext):
        if ctx.getChildCount()>1:
            return self.visit(ctx.class_mem_decl())+self.visit(ctx.list_class_mem())
        return self.visit(ctx.class_mem_decl())
        
    
    def visitClass_mem_decl(self, ctx: D96Parser.Class_mem_declContext):
        if ctx.class_attr_decl():
            return self.visit(ctx.class_attr_decl())
        return self.visit(ctx.class_method_decl())
    
    def visitClass_attr_decl(self, ctx: D96Parser.Class_attr_declContext):
        decl_list=[]
        if ctx.attr1():
            decl_list=self.visit(ctx.attr1())
        elif ctx.attr2():
            decl_list=self.visit(ctx.attr2())
            decl_list=[decl_list[len(decl_list)-1]]+decl_list[:-1]
            for i in range(0 ,int((len(decl_list)-1)/2)):
                decl_list[1+i][1],decl_list[len(decl_list)-1-i][1]=decl_list[len(decl_list)-1-i][1],decl_list[1+i][1]

        ret=[]
        if ctx.VAR():
            for i in range(1,len(decl_list)):
                if str(decl_list[i][0])[3]=='$':
                    ret+=[AttributeDecl(Static(),VarDecl(decl_list[i][0],decl_list[0],decl_list[i][1]))]
                else:
                    ret+=[AttributeDecl(Instance(),VarDecl(decl_list[i][0],decl_list[0],decl_list[i][1]))]
        elif ctx.VAL():
            for i in range(1,len(decl_list)):
                if str(decl_list[i][0])[3]=='$':
                    ret+=[AttributeDecl(Static(),ConstDecl(decl_list[i][0],decl_list[0],decl_list[i][1]))]
                else:
                    ret+=[AttributeDecl(Instance(),ConstDecl(decl_list[i][0],decl_list[0],decl_list[i][1]))]
        return ret

    def visitAttr1(self, ctx: D96Parser.Attr1Context):
        ret=[self.visit(ctx.mptype())]
        ret+=self.visit(ctx.list_id())
        for i in range(1,len(ret)):
            ret[i]=(ret[i],None)
        return ret

    def visitAttr2(self, ctx: D96Parser.Attr2Context):
        ret=[]
        if ctx.attr2():
            ret+=[[self.visit(ctx.mpid()),self.visit(ctx.expr())]]
            ret+=self.visit(ctx.attr2())
            return ret
        elif ctx.mptype():
            ret+=[[self.visit(ctx.mpid()),self.visit(ctx.expr())]]+[self.visit(ctx.mptype())]
            return ret
    
    def visitList_id(self, ctx: D96Parser.List_idContext):
        if ctx.getChildCount()>1:
            return [self.visit(ctx.mpid())]+self.visit(ctx.list_id())
        return [self.visit(ctx.mpid())]
    
    def visitList_expr(self, ctx: D96Parser.List_exprContext):
        if ctx.getChildCount()>1:
            return [self.visit(ctx.expr())]+self.visit(ctx.list_expr())
        return [self.visit(ctx.expr())]
    
    def visitLiteral(self,ctx:D96Parser.LiteralContext):
        if ctx.LIT_INT():
            return IntLiteral(ctx.LIT_INT().getText())
        if ctx.LIT_FLOAT():
            return FloatLiteral(ctx.LIT_FLOAT().getText())
        if ctx.lit_boolean():
            return BooleanLiteral(self.visit(ctx.lit_boolean()))
        if ctx.LIT_STRING():
            return StringLiteral(ctx.LIT_STRING().getText())
        if ctx.lit_indexed_arr():
            return ArrayLiteral(self.visit(ctx.lit_indexed_arr()))
        if ctx.lit_mul_arr():
            return ArrayLiteral(self.visit(ctx.lit_mul_arr))

    def visitMptype(self,ctx:D96Parser.MptypeContext):
        if ctx.primitive_type():
            return self.visit(ctx.primitive_type())
        if ctx.array_type():
            return self.visit(ctx.array_type())
        if ctx.class_type():
            return self.visit(ctx.class_type())

    def visitClass_type(self,ctx:D96Parser.Class_typeContext):
        return ClassType(ctx.ID().getText())

    def visitPrimitive_type(self,ctx:D96Parser.Primitive_typeContext):
        if ctx.BOOLEAN():
            return BoolType()
        if ctx.INT():
            return IntType()
        if ctx.FLOAT():
            return FloatType()
        if ctx.STRING():
            return StringType()
        
    def visitArray_type(self,ctx:D96Parser.Array_typeContext):
        return self.visit(ctx.array_characteristic())

    def visitArray_characteristic(self,ctx:D96Parser.Array_characteristicContext):
        return ArrayType(self.visit(ctx.array_size()),self.visit(ctx.array_element_type()))

    def visitArray_size(self,ctx:D96Parser.ExprContext):
        return self.visit(ctx.expr())

    def visitArray_element_type(self,ctx:D96Parser.Array_element_typeContext):
        if ctx.primitive_type():
            return self.visit(ctx.primitive_type())
        return self.visit(ctx.array_type())

    def visitClass_method_decl(self,ctx:D96Parser.Class_method_declContext):
        if ctx.static_method():
            return [self.visit(ctx.static_method())]
        if ctx.instance_method():
            return [self.visit(ctx.instance_method())]
        if ctx.constructor_method():
            return [self.visit(ctx.constructor_method())]
        if ctx.destructor_method():
            return [self.visit(ctx.destructor_method())]

    def visitStatic_method(self,ctx:D96Parser.Static_methodContext):
        return MethodDecl(Static(),Id(ctx.ID_STATIC().getText()),self.visit(ctx.list_para()),self.visit(ctx.stat_block()))

    def visitInstance_method(self,ctx:D96Parser.Instance_methodContext):
        return MethodDecl(Instance(),Id(ctx.ID().getText()),self.visit(ctx.list_para()),self.visit(ctx.stat_block()))

    def visitConstructor_method(self,ctx:D96Parser.Constructor_methodContext):
        return MethodDecl(Instance(),Id("Constructor"),self.visit(ctx.list_para()),self.visit(ctx.stat_block()))
    
    def visitDestructor_method(self,ctx:D96Parser.Destructor_methodContext):
        return MethodDecl(Instance(),Id("Destructor"),[],self.visit(ctx.stat_block()))

    def visitList_para(self,ctx:D96Parser.List_paraContext):
        if ctx.getChildCount()>0:
            return self.visit(ctx.notnull_list_para())
        return []

    def visitNotnull_list_para(self,ctx:D96Parser.Notnull_list_paraContext):
        if ctx.getChildCount()>1:
            return self.visit(ctx.para())+self.visit(ctx.notnull_list_para())
        return self.visit(ctx.para())

    def visitPara(self,ctx:D96Parser.ParaContext):
        ret=[]
        listId=self.visit(ctx.list_id_ins())
        mtype=self.visit(ctx.mptype())
        for id in listId:
            ret+=[VarDecl(Id(id),mtype,None)]
        return ret

    def visitStat(self,ctx:D96Parser.StatContext):
        if ctx.stat_var_con():
            return self.visit(ctx.stat_var_con())
        if ctx.stat_assign():
            return self.visit(ctx.stat_assign())
        if ctx.stat_if():
            return [self.visit(ctx.stat_if())]
        if ctx.stat_foreach():
            return [self.visit(ctx.stat_foreach())]
        if ctx.stat_break():
            return [self.visit(ctx.stat_break())]
        if ctx.stat_continue():
            return [self.visit(ctx.stat_continue())]
        if ctx.stat_return():
            return [self.visit(ctx.stat_return())]
        if ctx.stat_method_ins():
            return [self.visit(ctx.stat_method_ins())]
        if ctx.stat_method_sta():
            return [self.visit(ctx.stat_method_sta())]
        if ctx.stat_block():
            return [self.visit(ctx.stat_block())]

    def visitStat_var_con(self,ctx:D96Parser.Stat_var_conContext):
        ret=[]
        if ctx.VAR():
            if ctx.stat_var_con1():
                listId = self.visit(ctx.stat_var_con1())
                for i in range(1,len(listId)):
                    ret+=[VarDecl(Id(listId[i]),listId[0],None)]

            elif ctx.stat_var_con2():
                listId = self.visit(ctx.stat_var_con2())
                listId = [listId[len(listId)-1]]+listId[:-1]
                for i in range(0,int((len(listId)-1)/2)):
                    listId[1+i][1],listId[len(listId)-1-i][1]=listId[len(listId)-1-i][1],listId[1+i][1]
                for i in range(1,len(listId)):
                    ret+=[VarDecl(Id(listId[i][0]),listId[0],listId[i][1])]


        if ctx.VAL():
            if ctx.stat_var_con1():
                listId = self.visit(ctx.stat_var_con1())
                for i in range(1,len(listId)):
                    ret+=[ConstDecl(Id(listId[i]),listId[0],None)]

            elif ctx.stat_var_con2():
                listId = self.visit(ctx.stat_var_con2())
                listId = [listId[len(listId)-1]]+listId[:-1]
                for i in range(0,int((len(listId)-1)/2)):
                    listId[1+i][1],listId[len(listId)-1-i][1]=listId[len(listId)-1-i][1],listId[1+i][1]
                for i in range(1,len(listId)):
                    ret+=[ConstDecl(Id(listId[i][0]),listId[0],listId[i][1])]
                    
        return ret

    def visitStat_var_con1(self,ctx:D96Parser.Stat_var_con1Context):
        x=[self.visit(ctx.mptype())]+self.visit(ctx.list_id_ins())
        return x
    
    def visitStat_var_con2(self,ctx:D96Parser.Stat_var_con2Context):
        if ctx.stat_var_con2():
            ret=[[ctx.ID().getText(),self.visit(ctx.expr())]]
            ret+=self.visit(ctx.stat_var_con2())
            return ret
        if ctx.mptype():
            return [[ctx.ID().getText(),self.visit(ctx.expr())]]+[self.visit(ctx.mptype())]
                       

    def visitList_id_ins(self,ctx:D96Parser.List_id_insContext):
        if ctx.getChildCount()>1:
            return [ctx.ID().getText()]+self.visit(ctx.list_id_ins())
        return [ctx.ID().getText()]
        
    def visitStat_assign(self,ctx:D96Parser.Stat_assignContext):
        return [Assign(self.visit(ctx.stat_assign_lhs()),self.visit(ctx.expr()))]
    
    def visitStat_assign_lhs(self,ctx:D96Parser.Stat_assign_lhsContext):
        if ctx.mpid():
            return self.visit(ctx.mpid())
        if ctx.expr7():
            return self.visit(ctx.expr7())

    def visitStat_if(self,ctx:D96Parser.Stat_ifContext):
        part_if = self.visit(ctx.part_if())
        return If(part_if[0],part_if[1],self.visit(ctx.list_else()))
    
    def visitPart_if(self,ctx:D96Parser.Part_ifContext):
        return (self.visit(ctx.expr()),self.visit(ctx.stat_block()))
    
    def visitList_else(self,ctx:D96Parser.List_elseContext):
        if ctx.getChildCount()==2:
            elseif=self.visit(ctx.elseif())
            return If(elseif[0],elseif[1],self.visit(ctx.list_else()))
        elif ctx.getChildCount()==1:
            return self.visit(ctx.part_else())
        elif ctx.getChildCount()==0:
            return None
        
    def visitElseif(self,ctx:D96Parser.ElseifContext):
        return (self.visit(ctx.expr()),self.visit(ctx.stat_block()))
    
    def visitPart_else(self,ctx:D96Parser.Part_elseContext):
        return self.visit(ctx.stat_block())
    
    def visitStat_foreach(self,ctx:D96Parser.Stat_foreachContext):
        return For(self.visit(ctx.mpid()),self.visit(ctx.for_expr1()),self.visit(ctx.for_expr2()),self.visit(ctx.stat_block()),self.visit(ctx.by_expr()))
        
    def visitFor_expr1(self,ctx:D96Parser.For_expr1Context):
        return self.visit(ctx.expr())
        
    def visitFor_expr2(self,ctx:D96Parser.For_expr2Context):
        return self.visit(ctx.expr())            

    def visitBy_expr(self,ctx:D96Parser.By_exprContext):
        if ctx.expr():
            return self.visit(ctx.expr())
        return None

    def visitStat_break(self,ctx:D96Parser.Stat_breakContext):
        return Break()

    def visitStat_continue(self,ctx:D96Parser.Stat_continueContext):
        return Continue()

    def visitStat_return(self,ctx:D96Parser.Stat_returnContext):
        if ctx.expr():
            return Return(self.visit(ctx.expr()))
        return Return(None)

    def visitStat_method_sta(self,ctx:D96Parser.Stat_method_staContext):
        if ctx.list_expr():
            return CallStmt(Id(ctx.ID().getText()),Id(ctx.ID_STATIC().getText()),self.visit(ctx.list_expr()))
        return CallStmt(Id(ctx.ID().getText()),Id(ctx.ID_STATIC().getText()),[])
        
    def visitStat_method_ins(self,ctx:D96Parser.Stat_method_insContext):
        if ctx.list_expr():
            return CallStmt(self.visit(ctx.expr8()),Id(ctx.ID().getText()),self.visit(ctx.list_expr()))
        return CallStmt(self.visit(ctx.expr8()),Id(ctx.ID().getText()),[])

    def visitStat_block(self,ctx:D96Parser.Stat_blockContext):
        return Block(self.visit(ctx.block_body()))
    
    def visitBlock_body(self,ctx:D96Parser.Block_bodyContext):
        if ctx.list_stat():
            return self.visit(ctx.list_stat())
        return []

    def visitList_stat(self,ctx:D96Parser.List_statContext):
        if ctx.getChildCount()==2:
            return self.visit(ctx.stat())+self.visit(ctx.list_stat())
        return self.visit(ctx.stat())

    def visitExpr(self,ctx:D96Parser.ExprContext):
        if ctx.getChildCount() > 1:
            return BinaryOp(self.visit(ctx.op_string()),self.visit(ctx.expr1()[0]),self.visit(ctx.expr1()[1]))
        return self.visit(ctx.expr1()[0])

    def visitExpr1(self,ctx:D96Parser.Expr1Context):
        if ctx.getChildCount() > 1:
            return BinaryOp(self.visit(ctx.op_rel()),self.visit(ctx.expr2()[0]),self.visit(ctx.expr2()[1]))
        return self.visit(ctx.expr2()[0])

    def visitExpr2(self,ctx:D96Parser.Expr2Context):
        if ctx.getChildCount() > 1:
            return BinaryOp(self.visit(ctx.op_log2()),self.visit(ctx.expr2()),self.visit(ctx.expr3()))
        return self.visit(ctx.expr3())

    def visitExpr3(self,ctx:D96Parser.Expr3Context):
        if ctx.getChildCount() > 1:
            return BinaryOp(self.visit(ctx.op_add()),self.visit(ctx.expr3()),self.visit(ctx.expr4()))  
        return self.visit(ctx.expr4())

    def visitExpr4(self,ctx:D96Parser.Expr4Context):
        if ctx.getChildCount() > 1:
            return BinaryOp(self.visit(ctx.op_mul()),self.visit(ctx.expr4()),self.visit(ctx.expr5()))
        return self.visit(ctx.expr5())

    def visitExpr5(self,ctx:D96Parser.Expr5Context):
        if ctx.getChildCount() > 1:
            return UnaryOp(self.visit(ctx.op_log1()),self.visit(ctx.expr5()))
        return self.visit(ctx.expr6())

    def visitExpr6(self,ctx:D96Parser.Expr6Context):
        if ctx.getChildCount() > 1:
            return UnaryOp(ctx.MINUS().getText(),self.visit(ctx.expr6()))
        return self.visit(ctx.expr7())

    def visitExpr7(self,ctx:D96Parser.Expr7Context):
        if ctx.getChildCount() > 1:
            lst = self.visit(ctx.expr8())
            if isinstance(lst,list):
                lst+=[self.visit(ctx.expr())]
            else:
                lst=[lst]+[self.visit(ctx.expr())]
            return ArrayCell(lst[0],lst[1:])
        return self.visit(ctx.expr9()) 

    def visitExpr8(self,ctx:D96Parser.Expr8Context):
        if ctx.getChildCount() > 1:
            lst = self.visit(ctx.expr8())
            if isinstance(lst,list):
                return lst+[self.visit(ctx.expr())]
            else:
                return [lst]+[self.visit(ctx.expr())]
        return self.visit(ctx.expr9())

    def visitExpr9(self,ctx:D96Parser.Expr9Context):
        if ctx.getChildCount() == 3:
            return FieldAccess(self.visit(ctx.expr9()),Id(ctx.ID().getText()))
        if ctx.getChildCount() > 3:
            if ctx.list_expr():
                return CallExpr(self.visit(ctx.expr9()),Id(ctx.ID().getText()),self.visit(ctx.list_expr()))
            return CallExpr(self.visit(ctx.expr9()),Id(ctx.ID().getText()),[])
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr10())
    def visitExpr10(self,ctx:D96Parser.Expr10Context):
        if ctx.getChildCount()==3:
            return FieldAccess(Id(ctx.ID().getText()),Id(ctx.ID_STATIC().getText()))
        if ctx.getChildCount()>3:
            if ctx.list_expr():
                return CallExpr(Id(ctx.ID().getText()),Id(ctx.ID_STATIC().getText()),self.visit(ctx.list_expr()))
            return CallExpr(Id(ctx.ID().getText()),Id(ctx.ID_STATIC().getText()),[])
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr11())

    def visitExpr11(self,ctx:D96Parser.Expr11Context):
        if ctx.getChildCount()>1:
            if ctx.list_expr():
                return NewExpr(ctx.ID().getText(),self.visit(ctx.list_expr()))
            return NewExpr(ctx.ID().getText(),[])
        return self.visit(ctx.factor())
    
    def visitFactor(self,ctx:D96Parser.FactorContext):
        if ctx.mpid():
            return self.visit(ctx.mpid())
        if ctx.lit():
            return self.visit(ctx.lit())
        if ctx.expr():
            return self.visit(ctx.expr())
        if ctx.SELF():
            return SelfLiteral()
        if ctx.NULLS():
            return NullLiteral()

    def visitLit(self,ctx:D96Parser.LitContext):
        if ctx.LIT_INT():
            return (IntLiteral(ctx.LIT_INT().getText()))
        if ctx.LIT_STRING():
            return StringLiteral(ctx.LIT_STRING().getText())
        if ctx.LIT_FLOAT():
            return FloatLiteral(ctx.LIT_FLOAT().getText())
        if ctx.lit_boolean():
            return self.visit(ctx.lit_boolean())
        if ctx.lit_indexed_arr():
            return self.visit(ctx.lit_indexed_arr())
        if ctx.lit_mul_arr():
            return self.visit(ctx.lit_mul_arr())

    def visitOp_string(self,ctx:D96Parser.Op_stringContext):
        if ctx.EQUA_DOT():
            return ctx.EQUA_DOT().getText()
        if ctx.PLUS_DOT():
            return ctx.PLUS_DOT().getText()

    def visitOp_rel(self,ctx:D96Parser.Op_relContext):
        if ctx.EQUA():
            return ctx.EQUA().getText()
        if ctx.DIF():
            return ctx.DIF().getText()
        if ctx.LESS():
            return ctx.LESS().getText()
        if ctx.EQUA():
            return ctx.EQUA().getText()
        if ctx.DIF():
            return ctx.DIF().getText()
        if ctx.LESS():
            return ctx.LESS().getText()
        if ctx.MOREE():
            return ctx.MOREE().getText()
        if ctx.LESS_EQUA():
            return ctx.LESS_EQUA().getText()
        if ctx.MORE_EQUA():
            return ctx.MORE_EQUA().getText()

    def visitOp_log2(self,ctx:D96Parser.Op_log2Context):
        if ctx.AND():
            return ctx.AND().getText()
        if ctx.OR():
            return ctx.OR().getText()

    def visitOp_add(self,ctx:D96Parser.Op_addContext):
        if ctx.PLUS():
            return ctx.PLUS().getText()
        if ctx.MINUS():
            return ctx.MINUS().getText()
    
    def visitOp_mul(self,ctx:D96Parser.Op_mulContext):
        if ctx.MUL():
            return ctx.MUL().getText()
        if ctx.DIV():
            return ctx.DIV().getText()
        if ctx.PERCENT():
            return ctx.PERCENT().getText()

    def visitOp_log1(self,ctx:D96Parser.Op_log1Context):
        return ctx.EXCL().getText()

    def visitOp_obj(self,ctx:D96Parser.Op_objContext):
        return ctx.NEW().getText()


    def visitMpid(self,ctx:D96Parser.MpidContext):
        if ctx.ID():
            return Id(ctx.ID().getText())
        elif ctx.ID_STATIC():
            return Id(ctx.ID_STATIC().getText())
            
    def visitLit_boolean(self,ctx:D96Parser.Lit_booleanContext):
        if ctx.TRUES():
            return BooleanLiteral(ctx.TRUES().getText())
        return BooleanLiteral(ctx.FALSES().getText())
        
    def visitLit_indexed_arr(self,ctx:D96Parser.Lit_indexed_arrContext):
        return ArrayLiteral(self.visit(ctx.list_expr()))
    