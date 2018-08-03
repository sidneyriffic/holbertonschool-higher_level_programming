#!/bin/bash
# take URL as arg then curl get and print size of body
curl -sfL --max-redirs 0 "$1"
