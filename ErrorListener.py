import sys
from antlr4 import *
from MathOpParser import MathOpParser
from MathOpListener import MathOpListener
from antlr4.error.ErrorListener import *
import io


class ChatErrorListener(ErrorListener):
    def __init__(self, output):
        self.output = output
        self._symbol = ''

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.output.write(msg)
        self._symbol = offendingSymbol.text

    @property
    def symbol(self):
        return self._symbol