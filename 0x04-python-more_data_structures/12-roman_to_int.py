#!/usr/bin/python3
def roman_to_int(roman_string):
    ans = 0
    my_dict = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "I": 1, "V": 5}

    for i in range(len(roman_string)):
        if (i + 1 < len(roman_string) and
                my_dict[roman_string[i]] < my_dict[roman_string[i + 1]]):
            ans -= my_dict[roman_string[i]]
        else:
            ans += my_dict[roman_string[i]]
    return (ans);
