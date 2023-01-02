#!/usr/bin/python3
"""This file handles urllib.error.HTTPError error"""
from urllib import request, error
import sys


if __name__ == "__main__":
    try:
        with request.urlopen(sys.argv[1]) as response:
            print(response.read().decode())
    except error.HTTPError as e:
        print("Error code: {}".format(e.getcode()))
