#/usr/bin/python3
def multiply_by_2(a_dictionary):
    my_dict = {}
    for key in a_dictionary:
        my_dict[key] = a_dictionary[key] * 2
    return my_dict
