#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    return [list(map(lambda q: q*q, row)) for row in matrix]
