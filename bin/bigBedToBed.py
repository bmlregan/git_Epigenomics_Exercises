#!/usr/bin/env python3
import sys
import pyBigWig

infile = sys.argv[1]
outfile = sys.argv[2]

bb = pyBigWig.open(infile)

with open(outfile, "w") as out:
    for chrom, size in bb.chroms().items():
        entries = bb.entries(chrom, 0, size)
        if entries is None:
            continue
        for start, end, rest in entries:
            if rest:
                out.write(f"{chrom}\t{start}\t{end}\t{rest}\n")
            else:
                out.write(f"{chrom}\t{start}\t{end}\n")

bb.close()
