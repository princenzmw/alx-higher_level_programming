#!/usr/bin/python3

def roman_to_int(roman_string):
    if not roman_string:
        return 0
    elif type(roman_string) is not str:
        return 0

    result = 0
    rom_val = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}

    for rom_num in reversed(roman_string):
        int_num = rom_val[rom_num]
        result += int_num if result < int_num * 5 else -int_num
    return result
