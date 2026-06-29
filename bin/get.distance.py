#!/usr/bin/env python3

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--input", required=True)
parser.add_argument("--start", required=True, type=int)
args = parser.parse_args()

closest_gene = None
closest_start = None
closest_distance = None

with open(args.input) as f:
    for line in f:
        gene, start = line.strip().split("\t")
        start = int(start)
        distance = abs(args.start - start)

        if closest_distance is None or distance < closest_distance:
            closest_gene = gene
            closest_start = start
            closest_distance = distance

print(f"{closest_gene}\t{closest_start}\t{closest_distance}")
