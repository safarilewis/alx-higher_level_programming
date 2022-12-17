#!/usr/bin/python3
"""Fetches a url using urllib"""
import urllib.request


if __name__ == "__main__":
    print("Body response:")
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
        response = response.read()
    print("\t- type: {}".format(type(response)))
    print("\t- content: {}".format(response))
    print("\t- utf8 content: {}".format(response.decode("utf-8")))
