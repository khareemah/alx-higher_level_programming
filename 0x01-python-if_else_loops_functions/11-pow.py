#!/usr/bin/python3
def pow(a, b):
    result = 1
    for i in range(1, b + 1):
        result = result * a
    return result
