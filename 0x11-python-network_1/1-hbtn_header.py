#!/usr/bin/python3
"""This file takes a url and send a request"""
import urllib.request
import sys


if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        body = response.info()
        print(body['X-Request-Id'])
