#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if(idx < 0 or idx >= len(my_list)):
        return my_list
    new_list = my_list.copy()
    item_to_remove = new_list[idx]
    del item_to_remove
    return new_list
