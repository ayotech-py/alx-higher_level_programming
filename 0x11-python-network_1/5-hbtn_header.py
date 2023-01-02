#!/usr/bin/python3
"""The script fetchs a url and returns the X-Request-Id"""
import requests
import sys


if __name__ == "__main__":
    try:
        body = requests.get(sys.argv[1])
        print(body.headers['X-Request-Id'])
    except requests.exceptions.RequestException:
        pass
