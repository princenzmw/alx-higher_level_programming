#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result = []
    try:
        for i in range(list_length):
            try:
                division = my_list_1[i] / my_list_2[i]
                if not isinstance(division, (int, float)):
                    raise TypeError("wrong type")
                result.append(division)
            except ZeroDivisionError:
                print("division by 0")
                result.append(0)
            except (TypeError, IndexError):
                print("wrong type"
                      if isinstance(my_list_1[i], (int, float))
                      else "out of range")
                result.append(0)
    except IndexError:
        print("out of range")
        result.extend([0] * (list_length - len(result)))
    finally:
        return result
