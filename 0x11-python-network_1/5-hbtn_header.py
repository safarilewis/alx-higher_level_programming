#!/usr/bin/python3
"""Displays the value of a header"""
import requests
import sys


if __name__ == "__main__":
    response = requests.get(sys.argv[1], headers = X-Request-Id)
    print(response.content)
