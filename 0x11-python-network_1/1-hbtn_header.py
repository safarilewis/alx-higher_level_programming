#!/usr/bin/python3
"""Python script that takes in a url and displays the value of the X-Request-Id found in the header"""
import urllib.request
import sys

with urllib.request.urlopen(sys.argv[1]) as response:
    response = response.read()
print(response.get("X-Request-Id"))
