#!/usr/bin/python3
"""Script that sends a POST request"""
import sys
import urllib.request


if __name__ == "__main__":
    req = urllib.request.Request(sys.argv[1],sys.argv[2])
    with urllib.request.urlopen(req) as response:
        response = response.read()
    print("Your email is: {}".format(response))
