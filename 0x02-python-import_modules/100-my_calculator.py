#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div

if(__name__ == "__main__"):
    no_of_args = len(sys.argv)
    a = int(sys.argv[1])
    operator = sys.argv[2]
    b = int(sys.argv[3])

    if(no_of_args - 1 != 3):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    elif(operator == '+'):
        print("{} + {} = {}".format(a, b, add(a, b)))
    elif(operator == '-'):
        print("{} - {} = {}".format(a, b, sub(a, b)))
    elif(operator == '\*'):
        print("{} * {} = {}".format(a, b, mul(a, b)))
    elif(operator == '/'):
        print("{} / {} = {}".format(a, b, div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
    exit(1)
