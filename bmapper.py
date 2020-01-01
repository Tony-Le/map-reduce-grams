#!/usr/bin/python

import sys
import re
import csv

header = ["text", "date", "likes", "business_id", "user_id"]
reader = csv.reader(iter(sys.stdin.readline, ''))

# First line could be the HEADER, if it is, nothing gets outputted.
line1 = next(reader)
if line1 != header:
    # Tips are in the first column.
    tip = line1[0]
    tip = re.sub(r'^\W+|\W+$', '', tip)
    words = re.split(r"\W+", tip)

    # Output words in pairs. The last word in words will not have a pair next to it, so do not loop to that point.
    for i in range(len(words) - 1):
        print(words[i].lower() + " " + words[i + 1].lower() + "\t1")

for line in reader:
    tip = line[0]
    tip = re.sub(r'^\W+|\W+$', '', tip)
    words = re.split(r"\W+", tip)

    # Output words in pairs. The last word in words will not have a pair next to it, so do not loop to that point.
    for i in range(len(words) - 1):
        print(words[i].lower() + " " + words[i + 1].lower() + "\t1")