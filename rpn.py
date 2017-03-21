#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import operator
from termcolor import colored, cprint

OPERATORS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '^': operator.pow,
}


def calculate(arg):
    stack = list()
    for operand in arg.split():
        try:
            operand = float(operand)
            stack.append(operand)
        except:
            arg2 = stack.pop()
            arg1 = stack.pop()
            operator_fn = OPERATORS[operand]
            result = operator_fn(arg1, arg2)
            
            stack.append(result)
    return stack.pop()


def main():
    while True:
        try:
            result = calculate(input('rpn calc> '))
        except (KeyboardInterrupt, SystemExit):
            raise
        except:
            print("Try Again!")
            continue
        cprint('Result: ', 'yellow', attrs=['bold'], end='')
        str_result = str(result)
        if str_result[0] == '-':
            cprint(str_result[0], 'red', attrs=['bold'], end='')
            print(str_result[1:])
        else:
            print(str_result)


if __name__ == '__main__':
    main()

