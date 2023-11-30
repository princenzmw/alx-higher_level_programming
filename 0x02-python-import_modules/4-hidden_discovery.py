#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    names_in_module = [name for name in dir(hidden_4)
                       if not name.startswith('__')]
    sorted_names = sorted(names_in_module)

    for name in sorted_names:
        print(name)
