#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    row_list = []
    rows_list = []
    for rows in matrix:
        row_list = []
        for row in rows:
            row_list.append(row**2)
        rows_list.append(row_list)
    return rows_list
