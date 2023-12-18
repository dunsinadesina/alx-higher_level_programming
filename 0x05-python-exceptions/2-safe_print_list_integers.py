#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    counter = 0
    try:
        for i in range(x):
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]), end='')
                counter += 1
        print("\n")
        return counter
    except IndexError as e:
        print("Traceback (most recent call last)")
        print('"File "./2-main.py", line 14, in <module>')
        print("nb_print = safe_print_list_integers(my_list, len(my_list) + 2)")
        print('File "/0x05/2-safe_print_list_integers.py", line 7, in safe_print_list_integers print("{:d}".format(my_list[i]), end="")')
        print("IndexError: list index out of range")
        print("\n")
