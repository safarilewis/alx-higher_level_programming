#!/usr/bin/python3
"""Fetches a url using urllib"""
import urllib.request

with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    response = response.info()
