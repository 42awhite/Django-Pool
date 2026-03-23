#!/bin/sh

curl -sI "http://$1" | grep -i "^location:" | cut -d" " -f2 | tr -d "\r"
