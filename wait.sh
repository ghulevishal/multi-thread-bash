#!/bin/bash

filename=$(cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w 10 | head -n 1)
echo "Creating file: ${filename}, and going to sleep for 20 mins"
touch ${filename}
#sleep 3
echo "I'm done"
