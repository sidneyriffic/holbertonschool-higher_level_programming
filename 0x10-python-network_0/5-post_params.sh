#!/bin/bash
# take URL as arg then curl post with custom fields
curl -d"email=hr@holbertonschool.com&subject=I will always be here for PLD" "$1"
