#!/usr/bin/env python3
"""
Script to remove console.log and console.warn statements from index.html
while preserving console.error statements
"""

import re

# Read the file
with open('templates/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Count before
log_count = len(re.findall(r'^\s*console\.log\(.*?\);?\s*$', content, re.MULTILINE))
warn_count = len(re.findall(r'^\s*console\.warn\(.*?\);?\s*$', content, re.MULTILINE))

print(f"Found {log_count} console.log statements")
print(f"Found {warn_count} console.warn statements")

# Remove console.log lines (entire line including newline)
content = re.sub(r'^\s*console\.log\(.*?\);?\s*\n', '', content, flags=re.MULTILINE)

# Remove console.warn lines (entire line including newline)
content = re.sub(r'^\s*console\.warn\(.*?\);?\s*\n', '', content, flags=re.MULTILINE)

# Write back
with open('templates/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

# Count after
with open('templates/index.html', 'r', encoding='utf-8') as f:
    new_content = f.read()
    
log_count_after = len(re.findall(r'^\s*console\.log\(.*?\);?\s*$', new_content, re.MULTILINE))
warn_count_after = len(re.findall(r'^\s*console\.warn\(.*?\);?\s*$', new_content, re.MULTILINE))
error_count = len(re.findall(r'^\s*console\.error\(.*?\);?\s*$', new_content, re.MULTILINE))

print(f"\nAfter cleanup:")
print(f"  console.log: {log_count_after}")
print(f"  console.warn: {warn_count_after}")
print(f"  console.error (kept): {error_count}")
print(f"\nRemoved {(log_count + warn_count) - (log_count_after + warn_count_after)} statements")
