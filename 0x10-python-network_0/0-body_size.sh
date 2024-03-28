#!/bin/bash
# This script takes in a URL, sends a request to that URL
# and displays the size of the body of the response in bytes

url=$1
total_size=$(curl -sI $url | grep -i "content-length" | awk '{print $2}' | tr -d '\r')
echo $total_size
