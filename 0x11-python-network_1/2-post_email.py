#!/usr/bin/python3
""" a Python script that takes in a URL and an email"""
import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    val = {"Your email is": sys.argv[2]}
    data = urllib.parse.urlencode(val).encode("ascii")

    request = urllib.request.Request(url, data)
    with urllib.request.urlopen(request) as response:
        print(response.read().decode("utf-8"))
