#!/usr/bin/python3
def addargs(*args):
    if len(args) < 1:
        return
    result = 0
    for num in args:
        result += int(num)
    return result


if __name__ == "__main__":
    import sys
    arguments = sys.argv[1:]
    result = addargs(*arguments)
    print(result)
