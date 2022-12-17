#!/usr/bin/python3
"""Python script that takes in a url and displays the value of the X-Request-Id found in the header"""
import urllib.request
import sys


if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as request:
        response = request.read()
    print(request.get("X-Request-Id"))
