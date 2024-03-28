#!/bin/bash
# Bash script that takes in a URL, sends a request to that URL, and displays
#+	the size of the body of the response (in bytes) using 'curl'
curl -sI "$1" | awk '/Content-Length/{print $2}'
