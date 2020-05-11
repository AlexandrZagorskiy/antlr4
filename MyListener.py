# Generated from MathOp.g4 by ANTLR 4.8
from antlr4 import *
from tools import *

if __name__ is not None and "." in __name__:
    from .MathOpParser import MathOpParser
else:
    from MathOpParser import MathOpParser


# This class defines a complete listener for a parse tree produced by MathOpParser.
class MathOpListener(ParseTreeListener):
    pyFile = ""
    pyCode = ""
    tabCounter = 0

    # Enter a parse tree produced by MathOpParser#program.
    def enterProgram(self, ctx: MathOpParser.ProgramContext):
        print("Oh, hello there")

    # Exit a parse tree produced by MathOpParser#program.
    def exitProgram(self, ctx: MathOpParser.ProgramContext):
        self.pyCode += 'if __name__ == \'__main__\':\n    print(_main())\n'
        print("Good luck sir")
        self.pyFile = open("generated/MathOp.py", "w")
        self.pyFile.write(self.pyCode)
        self.pyFile.close()

    # Enter a parse tree produced by MathOpParser#subprog.
    def enterSubprog(self, ctx: MathOpParser.SubprogContext):
        self.pyCode += "def {}{}".format(str(ctx.FUNCNAME()), ctx.args().getText())

    # Exit a parse tree produced by MathOpParser#subprog.
    def exitSubprog(self, ctx: MathOpParser.SubprogContext):
        self.pyCode += '\n'

    # Enter a parse tree produced by MathOpParser#args.
    def enterArgs(self, ctx: MathOpParser.ArgsContext):
        pass

    # Exit a parse tree produced by MathOpParser#args.
    def exitArgs(self, ctx: MathOpParser.ArgsContext):
        pass

    # Enter a parse tree produced by MathOpParser#if_block.
    def enterIf_block(self, ctx: MathOpParser.If_blockContext):
        self.pyCode += "{}if {}".format('    ' * self.tabCounter, ctx.expression().getText())

    # Exit a parse tree produced by MathOpParser#if_block.
    def exitIf_block(self, ctx: MathOpParser.If_blockContext):
        pass

    # Enter a parse tree produced by MathOpParser#elif_block.
    def enterElif_block(self, ctx: MathOpParser.Elif_blockContext):
        self.pyCode += "{}elif {}".format('    ' * self.tabCounter, ctx.expression().getText())

    # Exit a parse tree produced by MathOpParser#elif_block.
    def exitElif_block(self, ctx: MathOpParser.Elif_blockContext):
        pass

    # Enter a parse tree produced by MathOpParser#else_block.
    def enterElse_block(self, ctx: MathOpParser.Else_blockContext):
        self.pyCode += "{}else".format('    ' * self.tabCounter)

    # Exit a parse tree produced by MathOpParser#else_block.
    def exitElse_block(self, ctx: MathOpParser.Else_blockContext):
        pass

    # Enter a parse tree produced by MathOpParser#block.
    def enterBlock(self, ctx: MathOpParser.BlockContext):
        self.pyCode += ':\n'
        self.tabCounter += 1

    # Exit a parse tree produced by MathOpParser#block.
    def exitBlock(self, ctx: MathOpParser.BlockContext):
        self.tabCounter -= 1

    # Enter a parse tree produced by MathOpParser#printexpression.
    def enterPrintexpression(self, ctx: MathOpParser.PrintexpressionContext):
        self.pyCode += '    ' * self.tabCounter + ctx.expression().getText()

    # Exit a parse tree produced by MathOpParser#printexpression.
    def exitPrintexpression(self, ctx: MathOpParser.PrintexpressionContext):
        self.pyCode += '\n'

    # Enter a parse tree produced by MathOpParser#ifelseBlock.
    def enterIfelseBlock(self, ctx: MathOpParser.IfelseBlockContext):
        pass

    # Exit a parse tree produced by MathOpParser#ifelseBlock.
    def exitIfelseBlock(self, ctx: MathOpParser.IfelseBlockContext):
        pass

    # Enter a parse tree produced by MathOpParser#return.
    def enterReturn(self, ctx: MathOpParser.ReturnContext):
        self.pyCode += '    ' * self.tabCounter + 'return {}'.format(ctx.expression().getText())

    # Exit a parse tree produced by MathOpParser#return.
    def exitReturn(self, ctx: MathOpParser.ReturnContext):
        self.pyCode += '\n\n'

    # Enter a parse tree produced by MathOpParser#eqExpression.
    def enterEqExpression(self, ctx: MathOpParser.EqExpressionContext):
        pass

    # Exit a parse tree produced by MathOpParser#eqExpression.
    def exitEqExpression(self, ctx: MathOpParser.EqExpressionContext):
        pass

    # Enter a parse tree produced by MathOpParser#addExpression.
    def enterAddExpression(self, ctx: MathOpParser.AddExpressionContext):
        pass

    # Exit a parse tree produced by MathOpParser#addExpression.
    def exitAddExpression(self, ctx: MathOpParser.AddExpressionContext):
        pass

    # Enter a parse tree produced by MathOpParser#compExpression.
    def enterCompExpression(self, ctx: MathOpParser.CompExpressionContext):
        pass

    # Exit a parse tree produced by MathOpParser#compExpression.
    def exitCompExpression(self, ctx: MathOpParser.CompExpressionContext):
        pass

    # Enter a parse tree produced by MathOpParser#exprExpression.
    def enterExprExpression(self, ctx: MathOpParser.ExprExpressionContext):
        pass

    # Exit a parse tree produced by MathOpParser#exprExpression.
    def exitExprExpression(self, ctx: MathOpParser.ExprExpressionContext):
        pass

    # Enter a parse tree produced by MathOpParser#atomExpression.
    def enterAtomExpression(self, ctx: MathOpParser.AtomExpressionContext):
        pass

    # Exit a parse tree produced by MathOpParser#atomExpression.
    def exitAtomExpression(self, ctx: MathOpParser.AtomExpressionContext):
        pass

    # Enter a parse tree produced by MathOpParser#powExpression.
    def enterPowExpression(self, ctx: MathOpParser.PowExpressionContext):
        pass

    # Exit a parse tree produced by MathOpParser#powExpression.
    def exitPowExpression(self, ctx: MathOpParser.PowExpressionContext):
        pass

    # Enter a parse tree produced by MathOpParser#multExpression.
    def enterMultExpression(self, ctx: MathOpParser.MultExpressionContext):
        pass

    # Exit a parse tree produced by MathOpParser#multExpression.
    def exitMultExpression(self, ctx: MathOpParser.MultExpressionContext):
        pass

    # Enter a parse tree produced by MathOpParser#funcCall.
    def enterFuncCall(self, ctx: MathOpParser.FuncCallContext):
        pass

    # Exit a parse tree produced by MathOpParser#funcCall.
    def exitFuncCall(self, ctx: MathOpParser.FuncCallContext):
        pass

    # Enter a parse tree produced by MathOpParser#assign.
    def enterAssign(self, ctx: MathOpParser.AssignContext):
        pass

    # Exit a parse tree produced by MathOpParser#assign.
    def exitAssign(self, ctx: MathOpParser.AssignContext):
        pass

    # Enter a parse tree produced by MathOpParser#Num.
    def enterNum(self, ctx: MathOpParser.NumContext):
        pass

    # Exit a parse tree produced by MathOpParser#Num.
    def exitNum(self, ctx: MathOpParser.NumContext):
        pass

    # Enter a parse tree produced by MathOpParser#Id.
    def enterId(self, ctx: MathOpParser.IdContext):
        pass

    # Exit a parse tree produced by MathOpParser#Id.
    def exitId(self, ctx: MathOpParser.IdContext):
        pass

    # Enter a parse tree produced by MathOpParser#Float.
    def enterFloat(self, ctx: MathOpParser.FloatContext):
        pass

    # Exit a parse tree produced by MathOpParser#Float.
    def exitFloat(self, ctx: MathOpParser.FloatContext):
        pass

    # Enter a parse tree produced by MathOpParser#Int.
    def enterInt(self, ctx: MathOpParser.IntContext):
        pass

    # Exit a parse tree produced by MathOpParser#Int.
    def exitInt(self, ctx: MathOpParser.IntContext):
        pass

    # Enter a parse tree produced by MathOpParser#types.
    def enterTypes(self, ctx: MathOpParser.TypesContext):
        pass

    # Exit a parse tree produced by MathOpParser#types.
    def exitTypes(self, ctx: MathOpParser.TypesContext):
        pass


del MathOpParser
