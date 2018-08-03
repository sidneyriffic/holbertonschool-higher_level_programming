#!/bin/bash
# take URL as arg then curl get and print size of body
if [ "$(curl -sI "$1" | head -1 | cut -f 2 -d " ")" = "200" ]; then
    curl -s "$1"
fi
