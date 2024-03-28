#!/usr/bin/python3
"""a Python script that takes in a letter and sends a POST request"""
import sys
import requests


if __name__ == "__main__":
    letter = "" if len(sys.argv) == 1 else sys.argv[1]
    pLoad = {"q": letter}

    a = requests.post("http://0.0.0.0:5000/search_user", data=pLoad)
    try:
        res = a.json()
        if res == {}:
            print("No result")
        else:
            print("[{}] {}".format(res.get("id"), res.get("name")))
    except ValueError:
        print("Not a valid JSON")
