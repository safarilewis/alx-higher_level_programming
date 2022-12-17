#!/usr/bin/python3
"""Displays the value of a header"""
import requests
import sys


if __name__ == "__main__":
    headers ={'X-Request-Id'}
    url = sys.argv[1]
    response = requests.get(url, headers = headers)
    print(response)
