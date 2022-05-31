#!/usr/bin/python3
def remove_char_at(str, n):
    new_string = ""
    if(n >= len(str) or n < 0):
        new_string = new_string + str
    else:
        for i in str:
            if(i == str[n]):
                continue
        new_string = new_string + i
    return new_string
