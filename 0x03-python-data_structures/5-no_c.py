#!/bin/bash
def no_c(my_string):
    if not my_string:
        return
    new_string = ""
    for i in my_string:
        if(i != "C" and i != "c"):
            new_string += i
    return new_string
