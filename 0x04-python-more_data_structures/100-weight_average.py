#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    sum_num = 0
    denum = 0
    for row in my_list:
        product = 1
        for col in row:
            product *= col
        sum_num += product
        denum += row[1]
    return sum_num / denum
