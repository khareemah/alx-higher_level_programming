#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    my_dict = {}
    for x in a_dictionary:
        my_dict[x] = a_dictionary[x] * 2
    return my_dict
