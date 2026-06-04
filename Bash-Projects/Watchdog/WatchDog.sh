#!/bin/bash

LOG_FILE=/home/gautham/Cloud-Learning/Bash-Projects/Watchdog/watchdog.log
log_message() {
    echo "$(date '+%Y-%m-%d %H:%M:%S') - $1" >> "$LOG_FILE"
}

echo "Enter the container name:"
read cont_name

cont_status=$(docker ps -a --filter "name=$cont_name" --format "{{.Status}}")
if [ -z "$cont_status" ]; then
    echo "$cont_name - Invalid Container Name"
    log_message "$cont_name Invalid Container Name"
else
    echo "$cont_status"
    log_message "$cont_status"
    if echo "$cont_status" | grep -q "Up"
    then
        echo "$cont_name - Container is running"
        log_message "$cont_name - Container is running"
    else
    echo "$cont_name - Container is not running, restarting ..."
    log_message "$cont_name - Container is not running, restarting ..."
    cont_restart=$(docker restart "$cont_name")
    echo "$cont_restart"
    log_message "Restarted - $cont_restart"
    fi
fi


