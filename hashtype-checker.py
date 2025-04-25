from hashid import HashID
from collections import defaultdict
from tqdm import tqdm
import glob

hash_counts = defaultdict(int)
scanner = HashID()

# Read and deduplicate all hashes from *.txt files
hashes = set()
print("Scanning hashes from: *.txt\n")
for file in glob.glob("*.txt"):
    print(f"Loading from: {file}")
    with open(file, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            line = line.strip()
            if line:
                hashes.add(line)

hashes = list(hashes)
print(f"\nTotal unique hashes: {len(hashes)}\n")

# Identify hash types with progress bar
for h in tqdm(hashes, desc="Checking hashes", unit="hash"):
    result = scanner.identifyHash(h)
    for item in result:
        hash_counts[item[0]] += 1

# Output summary
print("\n====== Hash Type Counts ======\n")
print(f"{'Hash Type':45} Count")
print(f"{'-'*45} {'-'*5}")
for htype, count in sorted(hash_counts.items(), key=lambda x: x[1], reverse=True):
    print(f"{htype:45} {count}")
