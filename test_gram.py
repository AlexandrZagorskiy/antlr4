import sys
from antlr4 import *
from MathOpLexer import MathOpLexer
from MathOpParser import MathOpParser


def main(argv):
    input = FileStream(argv[1])
    lexer = MathOpLexer(input)
    stream = CommonTokenStream(lexer)
    parser = MathOpParser(stream)
    tree = parser.program()
    print(tree.toStringTree(recog=parser))


if __name__ == '__main__':
    main(sys.argv)
