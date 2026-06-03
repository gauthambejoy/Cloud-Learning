#!/bin/bash

usage() {
    echo " $0 {Enter the number of processes} "
    echo " Example: $0 5 #Shows the Top 5 processes "
}

if [[ "$1" == "--help" || "$1" == "-h" ]]; then
    usage
    exit 0
fi

NUM_PROCESS=${1:-10}

if ! [[ "$NUM_PROCESS" =~ ^[0-9]+$ ]]; then
    echo "ERROR: Argument should be a numbber."
    exit 1
fi

echo "Top $NUM_PROCESS by CPU"
echo "--------------------------------------------"
ps -eo pid,user,%cpu,%mem,args | \
awk -v pid=$$ '$1 != pid' | \
sort -k3 -nr | \
awk -v n="$NUM_PROCESS" '
NR==1 {
    printf "%-8s %-12s %-6s %-6s %s\n", "PID", "USER", "CPU%", "MEM%", "COMMAND"
    next
}
NR<=n+1 {
    printf "%-8s %-12s %-6s %-6s %s\n", $1, $2, $3, $4, substr($0, index($0,$5))
}
' 

echo ""
echo "Top $NUM_PROCESS by MEM"
echo "--------------------------------------------"
ps -eo pid,user,%cpu,%mem,args | \
awk -v pid=$$ '$1 != pid' | \
sort -k4 -nr | \
awk -v n="$NUM_PROCESS" '
NR==1 {
    printf "%-8s %-12s %-6s %-6s %s\n", "PID", "USER", "CPU%", "MEM%", "COMMAND"
    next
}
NR<=n+1 {
    printf "%-8s %-12s %-6s %-6s %s\n", $1, $2, $3, $4, substr($0, index($0,$5))
}
'