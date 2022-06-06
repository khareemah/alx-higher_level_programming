#!/usr/bin/python3
def multiple_returns(sentence):
    my_len = len(sentence)
    if my_len == 0:
        return (my_len, None)
    return (my_len, sentence[0])
