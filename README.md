
# 🔍 Hash Type Aggregator

Tired of manually identifying hundreds of hashes with `hashid`?  
This script helps you **identify, count, and sort hash types** — fast and automated.

---

## 📦 Features

- Scans a file of hashes (default: `hashes.txt`, or pass a path as an argument)
- Identifies possible hash types using `hashid`
- Aggregates and **counts all detected types**
- Outputs a **sorted table** from most to least common

---

## 🧰 Requirements

- [`hashid`](https://github.com/psypanda/hashID)

Install it with:

```bash
pip install hashid
```

---

## 🚀 Usage

1. Save the script below as `typechecker.sh`
2. Make it executable:

```bash
chmod +x typechecker.sh
```

3. Run it (with optional path to your hash file):

```bash
./typechecker.sh path/to/your/hashes.txt
```

If no file is given, it defaults to `hashes.txt` in the same directory.

---

## 📜 Script: `typechecker.sh`

```bash
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
```

---

## 🧪 Tip

Pipe results into a file for saving reports:

```bash
./typechecker.sh path/to/hashes.txt > hash_summary.txt
```

---

## 🧙 About

This tool is made for pentesters, CTF players, and anyone with way too many hashes and not enough time.
