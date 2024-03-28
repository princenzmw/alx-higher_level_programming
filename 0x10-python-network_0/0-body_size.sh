#!/bin/bash
# Bash script takes in a URL, sends a request to that URL and displays the size of the body (comtent-lenght) of the response in bytes
curl -sI "$1" | awk '/Content-Length/{print $2}'
