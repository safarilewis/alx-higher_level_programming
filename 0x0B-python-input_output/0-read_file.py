#!/usr/bin/python3
"""Opening a file and reading it's contents"""


def read_file(filename=""):
    """Reading the file using with"""

    with open(filename, 'r',encoding = "utf-8") as f:
        read_data = f.read()
    print(read_data,end='')