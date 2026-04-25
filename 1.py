#!/usr/bin/env python3

import sys
import mwxml
import lzma
import csv

try:
    xml_file = sys.argv[1]
except IndexError:
    xml_file = "wikiruaruaru-20260423-wikidump/wikiruaruaru-20260423-history.xml"

try:
    dump = mwxml.Dump.from_file(open(xml_file, "r"))
except FileNotFoundError:
    raise Exception("Usage: python 1.py <xml_file: Wiki history dump> [output_file (data.csv)]")

revs = []
for page in dump:
    for rev in page:
        rev.page = page
        revs.append(rev)

revs.sort(key=lambda x: x.id)

namespaces = {}
for namespace in dump.site_info.namespaces:
    namespaces[namespace.id] = namespace.name

current = "" # "".join(map(lambda x: x.text or "", revs[:1234]))

size = old_size = 0

results = []

try:
    output_file = sys.argv[2]
except IndexError:
    output_file = "data.csv"

output = csv.writer(open(output_file, "w"))
output.writerow(["revid", "namespace", "page", "user", "size", "delta"])

progress = 0 # 1233
total_progress = len(revs)
rjust = len(str(total_progress))

for rev in revs: # revs[1234:]:
    current += rev.text or ""

    size = len(lzma.compress(bytes(current, "utf-8"), preset=lzma.PRESET_EXTREME))
    delta = size - old_size
    old_size = size

    namespace = namespaces[rev.page.namespace]
    result = [rev.id, namespace, rev.page.title.removeprefix(namespace + ":"), rev.user.text if rev.user else "", size, delta]

    results.append(result)

    output.writerow(result)

    progress += 1
    print(f"[{str(progress).rjust(rjust)} / {total_progress}]", result, sep="\t")
