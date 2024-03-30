#!/bin/bash
#a script that send a JSON POST request to a URL
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
