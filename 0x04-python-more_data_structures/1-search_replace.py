#!/usr/bin/python3
def search_replace(my_list, search, replace):
    # return ([num if num != search else replace for num in my_list])
    new_list = my_list.copy()
    for item in new_list:
        if item == search:
            new_list[search] = replace
    return new_list
