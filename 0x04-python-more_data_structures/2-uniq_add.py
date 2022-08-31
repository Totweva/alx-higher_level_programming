#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique = set(my_list)
    summ = 0
    for n in unique:
        summ += n
    return summ
