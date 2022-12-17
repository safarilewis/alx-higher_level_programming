#!/usr/bin/python3
"""Fetches a url using urllib"""
import urllib.request

if "__main__" == __name__:
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
        html = response.read()
