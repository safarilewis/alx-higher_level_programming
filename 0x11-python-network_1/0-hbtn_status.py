#!/usr/bin/python3
"""Fetches a url using urllib"""
import urllib.request

<<<<<<< HEAD
with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    response = response.info()
=======
if "__main__" == __name__:
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
        html = response.read()
>>>>>>> caaaa3503c0f85dc0a97897a2aa2dd83829e6d48
