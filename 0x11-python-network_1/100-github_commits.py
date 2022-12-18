#!/usr/bin/python3
"""Lists the last 10 commits for a given user"""
import sys
import requests


if __name__ == "__main__":
    response = requests.get("https://api.github.com/repos/{}/{}/commits".format(sys.argv[1], sys.argv[2]))
    x = 0
    while x < 10:
        print("{}: {}".format(response.get("sha"), response.get("commit").get("author").get("name")))
        x += 1
