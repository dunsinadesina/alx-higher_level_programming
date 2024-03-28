#!/usr/bin/python3
"""a Python script that takes your GitHub credentials"""
import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    a = requests.get("https://api.github.com/user", auth=auth)
    print(a.json().get("id"))
