#!/bin/bash

declare -A FILE_STATS

for f in $(ls -1 ../assets/questions/* | grep -E "*.md")
do
 FILE_STATS["$f"]=$(grep -c "$f" "$1")
 
done





for x in "${!FILE_STATS[@]}"; do printf "[%s] \t %s\n" "$x" "${FILE_STATS[$x]}" ; done | sort