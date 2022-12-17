#!/usr/bin/python3
"""Using requests package"""
import requests


if __name__ == "__main__":
    response = requests.get("https://alx-intranet.hbtn.io/status")
    print("\t- type: {}".format(type(response.text)))
    print("\t- content: {}".format(response.content))
