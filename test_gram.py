import sys
from antlr4 import *
from MathOpLexer import MathOpLexer
from MyListener import MathOpListener
from MathOpParser import MathOpParser


def main(argv):
    try:
        input = FileStream(argv[1])
    except IndexError:
        input = FileStream("tests/test5")
    lexer = MathOpLexer(input)
    stream = CommonTokenStream(lexer)
    parser = MathOpParser(stream)
    tree = parser.program()
    printer = MathOpListener()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)


if __name__ == '__main__':
    main(sys.argv)
