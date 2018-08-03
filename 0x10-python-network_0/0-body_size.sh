#!/bin/bash
# take URL as arg then curl get and print size of body
curl -sI "$1" | grep "Content-Length: " | cut -f 2 -d " "
