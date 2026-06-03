#!/bin/bash
echo "Enter the container name:"
read cont_name

cont_status=$(docker ps -a --filter "name=$cont_name" --format "{{.Status}}")
if [ -z "$cont_status" ]; then
    echo "Invalid Container Name"
else
    echo "$cont_status"
    if echo "$cont_status" | grep -q "Up"
    then
        echo "Container is running"
    else
    echo "Container is not running, restarting ..."
    cont_restart=$(docker restart $cont_name)
    echo "$cont_restart"
    fi
fi




