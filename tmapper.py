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

    # Output words and the next two words. Stop before the second last words since there will not be two more words at
    # that point.
    for i in range(len(words) - 2):
        print(words[i].lower() + " " + words[i + 1].lower() + " " + words[i + 2].lower() + "\t1")

for line in reader:
    tip = line[0]
    tip = re.sub(r'^\W+|\W+$', '', tip)
    words = re.split(r"\W+", tip)

    # Output words and the next two words. Stop before the second last words since there will not be two more words at
    # that point.
    for i in range(len(words) - 2):
        print(words[i].lower() + " " + words[i + 1].lower() + " " + words[i + 2].lower() + "\t1")