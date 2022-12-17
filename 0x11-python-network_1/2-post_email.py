#!/usr/bin/python3
"""Script that sends a POST request"""
import sys
import urllib.request
import urllib.parse


if __name__ == "__main__":
    url = sys.argv[1]
    value = sys.argv[2]
    #data = urllib.parse.urlencode(value)
    data = value.encode('ascii')
    req = urllib.request.Request(url,data)
    with urllib.request.urlopen(req) as response:
        response = response.read()
    print(response)
