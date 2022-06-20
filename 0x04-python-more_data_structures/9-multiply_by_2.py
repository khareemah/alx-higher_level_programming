#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    my_dict = {}
    for key, value in a_dictionary.items():
        my_dict[key] = value * 2
    return my_dict
