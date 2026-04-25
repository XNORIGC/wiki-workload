#!/usr/bin/env python3

import sys
import csv

try:
    csv_file = sys.argv[1]
except IndexError:
    csv_file = "data.csv"

try:
    reader = csv.reader(open(csv_file, "r"))
except FileNotFoundError:
    raise Exception("Usage: python 2.py [csv_file (data.csv): The output file from 1.py] [output_file (results.csv)]")

next(reader) # Skip header

results = {}
for row in reader:
    user = row[3]
    delta = int(row[5])
    results.setdefault(user, 0)
    results[user] += delta

results = list(results.items())
results.sort(key=lambda x: x[1], reverse=True)

try:
    output_file = sys.argv[2]
except IndexError:
    output_file = "results.csv"

output = csv.writer(open(output_file, "w"))
output.writerow(["user", "total workload"])
output.writerows(results)
