#!/usr/bin/python3
"""Displays the value of a header"""
import requests


if __name__ == "__main__":
    response = requests.get(sys.argv[1])
    print(response.info("X-Request-Id"))