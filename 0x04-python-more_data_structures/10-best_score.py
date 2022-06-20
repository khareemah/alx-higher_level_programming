#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
#    return max(a_dictionary, key=lambda k: a_dictionary[k])
    max_value = 0
    for key, value in a_dictionary:
        if value > max_value:
            max_value = value
    return key
