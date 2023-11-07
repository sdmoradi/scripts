#!/bin/bash

#Bash script that performs index deletion operations in Elasticsearch based on a specific pattern

PATTERN="2023-10"
USER="elastic"
PASSWORD="elastic"
HOST="localhost"
PORT="9200"

curl -u $USER:$PASSWORD -X GET http://$HOST:$PORT/_cat/indices?h=index | grep "$PATTERN" | awk '{print $1}' | xargs -I {} curl -u $USER:$PASSWORDi -X DELETE http://$HOST:$PORT/{}
