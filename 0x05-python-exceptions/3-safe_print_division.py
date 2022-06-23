#!/usr/bin/python3


def safe_print_division(a, b):
    result = 0
    print("Inside result: ", end='')
    try:
        result = a / b
    except:
        result = None
    finally:
        print("{}".format(result))
        return result
