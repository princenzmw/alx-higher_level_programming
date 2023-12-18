#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result = []
    quotient = 0

    for x in range(list_length):
        try:
            quotient = my_list_1[x] / my_list_2[x]
        except TypeError:
            print("wrong type")
            quotient = 0
        except ZeroDivisionError:
            print("Division by 0")
            quotient = 0
        except IndexError:
            print("out of range")
            quotient = 0
        finally:
            result.append(quotient)

    return result
