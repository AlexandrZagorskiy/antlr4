import re


def getOperSymb(token):
    oper = re.search(r'\'\S\'', token)
    oper = oper.group(0)[1:-1]
    return oper
