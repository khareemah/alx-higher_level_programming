#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    k = "None"
    for key, val in a_dictionary.items():
        if val == value:
           k = key
    if k in a_dictionary:
        del a_dictionary[k]
    return a_dictionary
