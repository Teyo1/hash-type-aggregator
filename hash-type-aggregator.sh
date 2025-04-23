#!/bin/bash

declare -A hash_types

echo -e "Scanning hashes from: hashes.txt\n"

while read -r line; do
    echo "Checking hash: $line"
    while IFS= read -r type; do
        echo "  Found type: $type"
        ((hash_types["$type"]++))
    done < <(hashid -m "$line" 2>/dev/null | sed -n 's/^\[+\] //p')
done < hashes.txt

echo -e "\n====== Hash Type Counts ======\n"
printf "%-45s %s\n" "Hash Type" "Count"
printf "%-45s %s\n" "---------" "-----"

for key in "${!hash_types[@]}"; do
    printf "%-45s %5d\n" "$key" "${hash_types[$key]}"
done | sort -k2 -nr
