#!/usr/bin/python3
def max_integer(my_list=[]):
    max_number = float('-inf')
    for i in my_list:
        if (i > max_number):
            max_number = i
    return max_number
