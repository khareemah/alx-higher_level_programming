#!/usr/bin/python3
def multiple_returns(sentence):
    my_list = [None]
    my_length = len(sentence)
    if my_length == 0:
        my_list[0] = None
    else:
        my_list[0] = my_length
    my_tuple = tuple(my_list)
    return my_length, sentence[0]
