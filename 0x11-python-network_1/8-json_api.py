#!/usr/bin/python3
"""This script does a lot of things"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) == 2:
        response = requests.post("http://0.0.0.0:5000/\
                search_user", data={'q': sys.argv[1]})
    else:
        response = requests.post("http://0.0.0.0:5000/\
                search_user", data={'q': ""})
    if response.json() and len(response.json()) != 0:
        print("[{}] {}".format(response.json()['id'], response.json()['name']))
    elif len(response.json()) == 0:
        print("No result")
    else:
        print("Not a valid JSON")
