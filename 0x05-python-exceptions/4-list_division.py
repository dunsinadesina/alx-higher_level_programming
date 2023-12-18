#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """Write a function that divides element by element 2 lists.
    Args:
        my_list_1: the first list
        my_list_2: the second list
        list_length: number of elements to divide
    Returns:
        a new list
    """
    new_list = []
    for i in range(0, list_length):
        try:
            div = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            div = 0
        except ZeroDivisionError:
            print("division by 0")
            div = 0
        except IndexError:
            print("out of range")
            div = 0
        finally:
            new_list.append(div)
    return(new_list)
