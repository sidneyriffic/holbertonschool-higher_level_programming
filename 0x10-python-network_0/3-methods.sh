#!/bin/bash
# take URL as arg then curl get and print size of body
curl -sI -X OPTIONS "$1" | grep "Allow: " | cut -f 2 -d " "
