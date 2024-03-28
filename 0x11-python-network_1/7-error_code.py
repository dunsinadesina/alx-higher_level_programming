#!/usr/bin/python3
"""a Python script that takes in a URL, sends a request to the URL"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    a = requests.get(url)
    if a.status_code >= 400:
        print("Error code: {}".format(a.status_code))
    else:
        print(a.text)
