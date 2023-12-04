#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        print()
        return
    for row in matrix:
        if not row:
            print()
            continue
        for i in row[:-1]:
            print("{:d}".format(i), end=" ")
        print("{:d}".format(row[-1]))
        if (row != matrix[-1]):
            print()
