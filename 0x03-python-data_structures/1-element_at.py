#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0:
        return None
    for i in my_list:
        if idx == i:
            print("Element at {:d} is {:d}".format(i, my_list[i]))
        elif idx > i:
            return None