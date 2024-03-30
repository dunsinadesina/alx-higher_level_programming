#!/bin/bash
#a script that takes in a URL as an argument, sends and displays a GET request
curl -sH "X-School-User-Id" "$1"
