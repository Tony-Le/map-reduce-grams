#!/usr/bin/python

import sys

previous = None
total = 0

for line in sys.stdin:
    key, value = line.split("\t")

    if key != previous:
        if previous is not None:
            # A new key is encountered that is not the first key. Print the previous key and its total.
            print(previous + '\t' + str(total))
        # Reset
        previous = key
        total = 0
    # If key is still the same, up the total.
    total = total + int(value)
# Print when reaching the end.
print(previous + '\t' + str(total))
