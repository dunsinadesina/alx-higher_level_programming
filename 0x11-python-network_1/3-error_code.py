#!/usr/bin/python3
"""a Python script that takes in a URL, sends a request to the URL"""
import sys
import urllib.error
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]

    request = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(request) as response:
            print(response.read().decode("ascii"))
    except urllib.error.HTTPError as r:
        print("Error code: {}".format(r.code))
