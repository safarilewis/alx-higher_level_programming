#!/usr/bin/python3
"""Searching json"""
import sys
import requests


if __name__ == "__main__":
    if sys.argv[1]:
        q = sys.argv[1]
    else:
        q = ""
    response = requests.get("http://0.0.0.0:5000/search_user",params=q)
    response.json()
