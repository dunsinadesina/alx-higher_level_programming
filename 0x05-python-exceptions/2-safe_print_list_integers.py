#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """ function that prints the first x elements of a list and only integers.
    Args:
        my_list[]: list to print element from
        x: the counter
    Return:
        number of elements print
    """
    counter = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            counter += 1
        except (ValueError, TypeError):
            continue
    print("")
    return counter
