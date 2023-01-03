#!/usr/bin/python3
"""The script sends a post request to a url"""
import requests
import sys


if __name__ == "__main__":
    body = requests.post(sys.argv[1], data = {'email': sys.argv[2]})
    print(body.text)
