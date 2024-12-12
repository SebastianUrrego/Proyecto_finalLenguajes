# Generated from asua.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .asuaParser import asuaParser
else:
    from asuaParser import asuaParser

# This class defines a complete listener for a parse tree produced by asuaParser.
class asuaListener(ParseTreeListener):

    # Enter a parse tree produced by asuaParser#program.
    def enterProgram(self, ctx:asuaParser.ProgramContext):
        pass

    # Exit a parse tree produced by asuaParser#program.
    def exitProgram(self, ctx:asuaParser.ProgramContext):
        pass


    # Enter a parse tree produced by asuaParser#importStatement.
    def enterImportStatement(self, ctx:asuaParser.ImportStatementContext):
        pass

    # Exit a parse tree produced by asuaParser#importStatement.
    def exitImportStatement(self, ctx:asuaParser.ImportStatementContext):
        pass


    # Enter a parse tree produced by asuaParser#statement.
    def enterStatement(self, ctx:asuaParser.StatementContext):
        pass

    # Exit a parse tree produced by asuaParser#statement.
    def exitStatement(self, ctx:asuaParser.StatementContext):
        pass


    # Enter a parse tree produced by asuaParser#logStatement.
    def enterLogStatement(self, ctx:asuaParser.LogStatementContext):
        pass

    # Exit a parse tree produced by asuaParser#logStatement.
    def exitLogStatement(self, ctx:asuaParser.LogStatementContext):
        pass


    # Enter a parse tree produced by asuaParser#assignment.
    def enterAssignment(self, ctx:asuaParser.AssignmentContext):
        pass

    # Exit a parse tree produced by asuaParser#assignment.
    def exitAssignment(self, ctx:asuaParser.AssignmentContext):
        pass


    # Enter a parse tree produced by asuaParser#expr.
    def enterExpr(self, ctx:asuaParser.ExprContext):
        pass

    # Exit a parse tree produced by asuaParser#expr.
    def exitExpr(self, ctx:asuaParser.ExprContext):
        pass


    # Enter a parse tree produced by asuaParser#list.
    def enterList(self, ctx:asuaParser.ListContext):
        pass

    # Exit a parse tree produced by asuaParser#list.
    def exitList(self, ctx:asuaParser.ListContext):
        pass


    # Enter a parse tree produced by asuaParser#array.
    def enterArray(self, ctx:asuaParser.ArrayContext):
        pass

    # Exit a parse tree produced by asuaParser#array.
    def exitArray(self, ctx:asuaParser.ArrayContext):
        pass


    # Enter a parse tree produced by asuaParser#accessArray.
    def enterAccessArray(self, ctx:asuaParser.AccessArrayContext):
        pass

    # Exit a parse tree produced by asuaParser#accessArray.
    def exitAccessArray(self, ctx:asuaParser.AccessArrayContext):
        pass


    # Enter a parse tree produced by asuaParser#matrix.
    def enterMatrix(self, ctx:asuaParser.MatrixContext):
        pass

    # Exit a parse tree produced by asuaParser#matrix.
    def exitMatrix(self, ctx:asuaParser.MatrixContext):
        pass


    # Enter a parse tree produced by asuaParser#row.
    def enterRow(self, ctx:asuaParser.RowContext):
        pass

    # Exit a parse tree produced by asuaParser#row.
    def exitRow(self, ctx:asuaParser.RowContext):
        pass


    # Enter a parse tree produced by asuaParser#matrixOperation.
    def enterMatrixOperation(self, ctx:asuaParser.MatrixOperationContext):
        pass

    # Exit a parse tree produced by asuaParser#matrixOperation.
    def exitMatrixOperation(self, ctx:asuaParser.MatrixOperationContext):
        pass


    # Enter a parse tree produced by asuaParser#conditional.
    def enterConditional(self, ctx:asuaParser.ConditionalContext):
        pass

    # Exit a parse tree produced by asuaParser#conditional.
    def exitConditional(self, ctx:asuaParser.ConditionalContext):
        pass


    # Enter a parse tree produced by asuaParser#loop.
    def enterLoop(self, ctx:asuaParser.LoopContext):
        pass

    # Exit a parse tree produced by asuaParser#loop.
    def exitLoop(self, ctx:asuaParser.LoopContext):
        pass


    # Enter a parse tree produced by asuaParser#parameters.
    def enterParameters(self, ctx:asuaParser.ParametersContext):
        pass

    # Exit a parse tree produced by asuaParser#parameters.
    def exitParameters(self, ctx:asuaParser.ParametersContext):
        pass


    # Enter a parse tree produced by asuaParser#arguments.
    def enterArguments(self, ctx:asuaParser.ArgumentsContext):
        pass

    # Exit a parse tree produced by asuaParser#arguments.
    def exitArguments(self, ctx:asuaParser.ArgumentsContext):
        pass


    # Enter a parse tree produced by asuaParser#functionDef.
    def enterFunctionDef(self, ctx:asuaParser.FunctionDefContext):
        pass

    # Exit a parse tree produced by asuaParser#functionDef.
    def exitFunctionDef(self, ctx:asuaParser.FunctionDefContext):
        pass


    # Enter a parse tree produced by asuaParser#functionCall.
    def enterFunctionCall(self, ctx:asuaParser.FunctionCallContext):
        pass

    # Exit a parse tree produced by asuaParser#functionCall.
    def exitFunctionCall(self, ctx:asuaParser.FunctionCallContext):
        pass


    # Enter a parse tree produced by asuaParser#returnStatement.
    def enterReturnStatement(self, ctx:asuaParser.ReturnStatementContext):
        pass

    # Exit a parse tree produced by asuaParser#returnStatement.
    def exitReturnStatement(self, ctx:asuaParser.ReturnStatementContext):
        pass


    # Enter a parse tree produced by asuaParser#graph.
    def enterGraph(self, ctx:asuaParser.GraphContext):
        pass

    # Exit a parse tree produced by asuaParser#graph.
    def exitGraph(self, ctx:asuaParser.GraphContext):
        pass


    # Enter a parse tree produced by asuaParser#primeGraph.
    def enterPrimeGraph(self, ctx:asuaParser.PrimeGraphContext):
        pass

    # Exit a parse tree produced by asuaParser#primeGraph.
    def exitPrimeGraph(self, ctx:asuaParser.PrimeGraphContext):
        pass


    # Enter a parse tree produced by asuaParser#rangeStart.
    def enterRangeStart(self, ctx:asuaParser.RangeStartContext):
        pass

    # Exit a parse tree produced by asuaParser#rangeStart.
    def exitRangeStart(self, ctx:asuaParser.RangeStartContext):
        pass


    # Enter a parse tree produced by asuaParser#rangeEnd.
    def enterRangeEnd(self, ctx:asuaParser.RangeEndContext):
        pass

    # Exit a parse tree produced by asuaParser#rangeEnd.
    def exitRangeEnd(self, ctx:asuaParser.RangeEndContext):
        pass


    # Enter a parse tree produced by asuaParser#step.
    def enterStep(self, ctx:asuaParser.StepContext):
        pass

    # Exit a parse tree produced by asuaParser#step.
    def exitStep(self, ctx:asuaParser.StepContext):
        pass


    # Enter a parse tree produced by asuaParser#fileOperation.
    def enterFileOperation(self, ctx:asuaParser.FileOperationContext):
        pass

    # Exit a parse tree produced by asuaParser#fileOperation.
    def exitFileOperation(self, ctx:asuaParser.FileOperationContext):
        pass


    # Enter a parse tree produced by asuaParser#kMeansOperation.
    def enterKMeansOperation(self, ctx:asuaParser.KMeansOperationContext):
        pass

    # Exit a parse tree produced by asuaParser#kMeansOperation.
    def exitKMeansOperation(self, ctx:asuaParser.KMeansOperationContext):
        pass


    # Enter a parse tree produced by asuaParser#regressionOperation.
    def enterRegressionOperation(self, ctx:asuaParser.RegressionOperationContext):
        pass

    # Exit a parse tree produced by asuaParser#regressionOperation.
    def exitRegressionOperation(self, ctx:asuaParser.RegressionOperationContext):
        pass


    # Enter a parse tree produced by asuaParser#mlpOperation.
    def enterMlpOperation(self, ctx:asuaParser.MlpOperationContext):
        pass

    # Exit a parse tree produced by asuaParser#mlpOperation.
    def exitMlpOperation(self, ctx:asuaParser.MlpOperationContext):
        pass



del asuaParser