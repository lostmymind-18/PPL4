# Generated from main/d96/parser/D96.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .D96Parser import D96Parser
else:
    from D96Parser import D96Parser

# This class defines a complete generic visitor for a parse tree produced by D96Parser.

class D96Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by D96Parser#program.
    def visitProgram(self, ctx:D96Parser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#list_class.
    def visitList_class(self, ctx:D96Parser.List_classContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#class_decl.
    def visitClass_decl(self, ctx:D96Parser.Class_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#class_block.
    def visitClass_block(self, ctx:D96Parser.Class_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#list_class_mem.
    def visitList_class_mem(self, ctx:D96Parser.List_class_memContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#class_mem_decl.
    def visitClass_mem_decl(self, ctx:D96Parser.Class_mem_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#class_attr_decl.
    def visitClass_attr_decl(self, ctx:D96Parser.Class_attr_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#attr1.
    def visitAttr1(self, ctx:D96Parser.Attr1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#attr2.
    def visitAttr2(self, ctx:D96Parser.Attr2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#list_id.
    def visitList_id(self, ctx:D96Parser.List_idContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#list_expr.
    def visitList_expr(self, ctx:D96Parser.List_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#literal.
    def visitLiteral(self, ctx:D96Parser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#mptype.
    def visitMptype(self, ctx:D96Parser.MptypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#class_type.
    def visitClass_type(self, ctx:D96Parser.Class_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#primitive_type.
    def visitPrimitive_type(self, ctx:D96Parser.Primitive_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#array_type.
    def visitArray_type(self, ctx:D96Parser.Array_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#array_characteristic.
    def visitArray_characteristic(self, ctx:D96Parser.Array_characteristicContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#array_element_type.
    def visitArray_element_type(self, ctx:D96Parser.Array_element_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#array_size.
    def visitArray_size(self, ctx:D96Parser.Array_sizeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#class_method_decl.
    def visitClass_method_decl(self, ctx:D96Parser.Class_method_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#static_method.
    def visitStatic_method(self, ctx:D96Parser.Static_methodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#instance_method.
    def visitInstance_method(self, ctx:D96Parser.Instance_methodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#constructor_method.
    def visitConstructor_method(self, ctx:D96Parser.Constructor_methodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#destructor_method.
    def visitDestructor_method(self, ctx:D96Parser.Destructor_methodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#list_para.
    def visitList_para(self, ctx:D96Parser.List_paraContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#notnull_list_para.
    def visitNotnull_list_para(self, ctx:D96Parser.Notnull_list_paraContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#para.
    def visitPara(self, ctx:D96Parser.ParaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#stat.
    def visitStat(self, ctx:D96Parser.StatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#stat_var_con.
    def visitStat_var_con(self, ctx:D96Parser.Stat_var_conContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#stat_var_con1.
    def visitStat_var_con1(self, ctx:D96Parser.Stat_var_con1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#stat_var_con2.
    def visitStat_var_con2(self, ctx:D96Parser.Stat_var_con2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#list_id_ins.
    def visitList_id_ins(self, ctx:D96Parser.List_id_insContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#stat_assign.
    def visitStat_assign(self, ctx:D96Parser.Stat_assignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#stat_assign_lhs.
    def visitStat_assign_lhs(self, ctx:D96Parser.Stat_assign_lhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#stat_if.
    def visitStat_if(self, ctx:D96Parser.Stat_ifContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#part_if.
    def visitPart_if(self, ctx:D96Parser.Part_ifContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#list_else.
    def visitList_else(self, ctx:D96Parser.List_elseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#elseif.
    def visitElseif(self, ctx:D96Parser.ElseifContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#part_else.
    def visitPart_else(self, ctx:D96Parser.Part_elseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#stat_foreach.
    def visitStat_foreach(self, ctx:D96Parser.Stat_foreachContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#for_expr1.
    def visitFor_expr1(self, ctx:D96Parser.For_expr1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#for_expr2.
    def visitFor_expr2(self, ctx:D96Parser.For_expr2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#by_expr.
    def visitBy_expr(self, ctx:D96Parser.By_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#stat_break.
    def visitStat_break(self, ctx:D96Parser.Stat_breakContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#stat_continue.
    def visitStat_continue(self, ctx:D96Parser.Stat_continueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#stat_return.
    def visitStat_return(self, ctx:D96Parser.Stat_returnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#stat_method_sta.
    def visitStat_method_sta(self, ctx:D96Parser.Stat_method_staContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#stat_method_ins.
    def visitStat_method_ins(self, ctx:D96Parser.Stat_method_insContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#stat_block.
    def visitStat_block(self, ctx:D96Parser.Stat_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#block_body.
    def visitBlock_body(self, ctx:D96Parser.Block_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#list_stat.
    def visitList_stat(self, ctx:D96Parser.List_statContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr.
    def visitExpr(self, ctx:D96Parser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr1.
    def visitExpr1(self, ctx:D96Parser.Expr1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr2.
    def visitExpr2(self, ctx:D96Parser.Expr2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr3.
    def visitExpr3(self, ctx:D96Parser.Expr3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr4.
    def visitExpr4(self, ctx:D96Parser.Expr4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr5.
    def visitExpr5(self, ctx:D96Parser.Expr5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr6.
    def visitExpr6(self, ctx:D96Parser.Expr6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr7.
    def visitExpr7(self, ctx:D96Parser.Expr7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr8.
    def visitExpr8(self, ctx:D96Parser.Expr8Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr9.
    def visitExpr9(self, ctx:D96Parser.Expr9Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr10.
    def visitExpr10(self, ctx:D96Parser.Expr10Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr11.
    def visitExpr11(self, ctx:D96Parser.Expr11Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#factor.
    def visitFactor(self, ctx:D96Parser.FactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#lit.
    def visitLit(self, ctx:D96Parser.LitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#op_string.
    def visitOp_string(self, ctx:D96Parser.Op_stringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#op_rel.
    def visitOp_rel(self, ctx:D96Parser.Op_relContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#op_log2.
    def visitOp_log2(self, ctx:D96Parser.Op_log2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#op_add.
    def visitOp_add(self, ctx:D96Parser.Op_addContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#op_mul.
    def visitOp_mul(self, ctx:D96Parser.Op_mulContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#op_log1.
    def visitOp_log1(self, ctx:D96Parser.Op_log1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#op_obj.
    def visitOp_obj(self, ctx:D96Parser.Op_objContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#mpid.
    def visitMpid(self, ctx:D96Parser.MpidContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#lit_boolean.
    def visitLit_boolean(self, ctx:D96Parser.Lit_booleanContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#lit_indexed_arr.
    def visitLit_indexed_arr(self, ctx:D96Parser.Lit_indexed_arrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#lit_mul_arr.
    def visitLit_mul_arr(self, ctx:D96Parser.Lit_mul_arrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#mul_arr_elements.
    def visitMul_arr_elements(self, ctx:D96Parser.Mul_arr_elementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#mul_arr_element.
    def visitMul_arr_element(self, ctx:D96Parser.Mul_arr_elementContext):
        return self.visitChildren(ctx)



del D96Parser