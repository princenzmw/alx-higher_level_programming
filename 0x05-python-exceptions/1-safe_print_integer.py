#!/usr/bin/python3

def safe_print_integer(value):
    status = False

    try:
        print("{:d}".format(value))
        status = True
    except:
        status = False

    return status
