#!/usr/bin/python3
"""This script list out 10 commit from a git repo"""
import requests
import sys


if __name__ == "__main__":
    user = sys.argv[2]
    repo = sys.argv[1]
    url = "https://api.github.com/repos/"+user+"/"+repo+"/commits"
    response = requests.get(url)
    data = response.json()
    for i in range(10):
        print("{}: {}".format(data[i]['sha'],
              data[i]['commit']['author']['name']))
