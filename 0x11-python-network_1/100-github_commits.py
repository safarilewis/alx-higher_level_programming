#!/usr/bin/python3
"""Lists the last 10 commits for a given user"""
import sys
import requests


if __name__ == "__main__":
    response = requests.get("https://api.github.com/repos/{}/{}/commits".format(sys.argv[1],
                                                    sys.argv[2]), params = {'per_page': 10})
    for commits in response.json():
        print("{}:{}".format(commits.get("sha"), commits.get("commit").get("author").get("name")))
   
