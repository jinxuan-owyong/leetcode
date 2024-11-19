from addEntry import addEntry
import re

with open(f'./README.md', 'r') as f:
    lines = [line for line in f]

# 0-based index
ENTRIES_BEGIN = 4
for i in range(ENTRIES_BEGIN, len(lines)):
    line = list(map(str.strip, lines[i].split('|')[1:-1]))
    num, problemRaw, solutions, difficulty = line
    nameMatcher = r'^\[(.+)\]\(https://.+\)$'
    problemName = hasLink.group(1) if (
        hasLink := re.search(nameMatcher, problemRaw)) else problemRaw

    if re.search(r'\[C\]', solutions):
        addEntry(int(num), problemName, difficulty, 'c', False)
    if re.search(r'\[C\+\+\]', solutions):
        addEntry(int(num), problemName, difficulty, 'cpp', False)
    if re.search(r'\[JavaScript\]', solutions):
        addEntry(int(num), problemName, difficulty, 'js', False)
    if re.search(r'\[Python\]', solutions):
        addEntry(int(num), problemName, difficulty, 'py', False)
    if re.search(r'\[SQL\]', solutions):
        addEntry(int(num), problemName, difficulty, 'sql', False)
