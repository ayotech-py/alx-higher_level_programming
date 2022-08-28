#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for nested_row in row:
            if row.index(nested_row) != 2:
                print("{:d}".format(nested_row), end=" ")
            else:
                print("{:d}".format(nested_row))
