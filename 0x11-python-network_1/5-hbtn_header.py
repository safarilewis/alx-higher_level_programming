#!/usr/bin/python3
"""Displays the value of a header"""
import requests
import sys


if __name__ == "__main__":
    headers ={'X-Request-Id'}
    response = requests.get(sys.argv[1], headers = headers)
    print(response.content)
