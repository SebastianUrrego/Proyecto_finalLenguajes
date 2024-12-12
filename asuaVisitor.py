# Generated from asua.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .asuaParser import asuaParser
else:
    from asuaParser import asuaParser

# This class defines a complete generic visitor for a parse tree produced by asuaParser.

class asuaVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by asuaParser#program.
    def visitProgram(self, ctx:asuaParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asuaParser#importStatement.
    def visitImportStatement(self, ctx:asuaParser.ImportStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asuaParser#statement.
    def visitStatement(self, ctx:asuaParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asuaParser#logStatement.
    def visitLogStatement(self, ctx:asuaParser.LogStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asuaParser#assignment.
    def visitAssignment(self, ctx:asuaParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asuaParser#expr.
    def visitExpr(self, ctx:asuaParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asuaParser#list.
    def visitList(self, ctx:asuaParser.ListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asuaParser#array.
    def visitArray(self, ctx:asuaParser.ArrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asuaParser#accessArray.
    def visitAccessArray(self, ctx:asuaParser.AccessArrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asuaParser#matrix.
    def visitMatrix(self, ctx:asuaParser.MatrixContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asuaParser#row.
    def visitRow(self, ctx:asuaParser.RowContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asuaParser#matrixOperation.
    def visitMatrixOperation(self, ctx:asuaParser.MatrixOperationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asuaParser#conditional.
    def visitConditional(self, ctx:asuaParser.ConditionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asuaParser#loop.
    def visitLoop(self, ctx:asuaParser.LoopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asuaParser#parameters.
    def visitParameters(self, ctx:asuaParser.ParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asuaParser#arguments.
    def visitArguments(self, ctx:asuaParser.ArgumentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asuaParser#functionDef.
    def visitFunctionDef(self, ctx:asuaParser.FunctionDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asuaParser#functionCall.
    def visitFunctionCall(self, ctx:asuaParser.FunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asuaParser#returnStatement.
    def visitReturnStatement(self, ctx:asuaParser.ReturnStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asuaParser#graph.
    def visitGraph(self, ctx:asuaParser.GraphContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asuaParser#primeGraph.
    def visitPrimeGraph(self, ctx:asuaParser.PrimeGraphContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asuaParser#rangeStart.
    def visitRangeStart(self, ctx:asuaParser.RangeStartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asuaParser#rangeEnd.
    def visitRangeEnd(self, ctx:asuaParser.RangeEndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asuaParser#step.
    def visitStep(self, ctx:asuaParser.StepContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asuaParser#fileOperation.
    def visitFileOperation(self, ctx:asuaParser.FileOperationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asuaParser#kMeansOperation.
    def visitKMeansOperation(self, ctx:asuaParser.KMeansOperationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asuaParser#regressionOperation.
    def visitRegressionOperation(self, ctx:asuaParser.RegressionOperationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by asuaParser#mlpOperation.
    def visitMlpOperation(self, ctx:asuaParser.MlpOperationContext):
        return self.visitChildren(ctx)



del asuaParser