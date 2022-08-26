#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 or idx > (len(my_list) - 1):
        i = my_list.copy()
        return i
    else:
        i[idx] = element
        return i
