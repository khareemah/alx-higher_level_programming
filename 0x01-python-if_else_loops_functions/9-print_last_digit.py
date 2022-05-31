#!/usr/bin/python3
def print_last_digit(number):
    last_digit = None
    if(number < 0):
        last_digit = (-1 * number) % 10
    else:
        last_digit = number % 10
    return last_digit
