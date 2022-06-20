#!/usr/bin/python3
def search_replace(my_list, search, replace):
    # return ([num if num != search else replace for num in my_list])
    new_list = my_list.copy()
    for index in range(len(new_list)):
        if new_list[index] == search:
            new_list[index] = replace
    return new_list
