#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for nested_row in row:
            print("{:d}".format(nested_row), end=" ")
        print("")
