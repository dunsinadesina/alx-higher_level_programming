#!/bin/bash
#a Bash script that takes in  a URL and displays the size of the body
curl -s "$1" | wc -c
