#!/usr/bin/python3
"""a Python script that takes in a URL and an email address"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    a = requests.get(url)
    print(a.headers.get("X-Request-Id"))
