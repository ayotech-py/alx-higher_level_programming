#!/usr/bin/python3
"""This script does a lot of things"""
import requests
import sys


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    if len(sys.argv) == 2:
        response = requests.post(url, data={'q': sys.argv[1]})
    else:
        response = requests.post(url, data={'q': ""})
    try:
        if response.json() and len(response.json()) != 0:
            print("[{}] {}".format(response.json()['id'], response.json()['name']))
        elif len(response.json()) == 0:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
