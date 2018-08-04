#!/bin/bash
# take URL as arg then curl get with custom header
curl -s --header "X-HolbertonSchool-User-Id: 98" "$1"
