#!/bin/bash
#a script that sends a request to the URL as an arg and displays the statuscode
curl -s -o /dev/null -w "%{http_code}" "$1"
