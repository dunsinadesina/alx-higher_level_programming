#!/bin/bash
#a script that takes a URL and displays the HTTP methods the server will accept
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
