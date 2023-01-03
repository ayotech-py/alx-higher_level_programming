#!/usr/bin/python3
"""This script used github api"""
import requests
import sys


if __name__ == "__main__":
    response = requests.get("https://api.github.com/user",
                            auth=(sys.argv[1], sys.argv[2]))
    if response.status_code == 200:
        print(response.json()['id'])
    else:
        print("None")
