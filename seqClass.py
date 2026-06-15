#!/usr/bin/env python

import sys, re
from argparse import ArgumentParser

# setting up command line arguments
parser = ArgumentParser(description='Classify a sequence as DNA or RNA')
parser.add_argument("-s", "--seq", type=str, required=True, help="Input sequence")
parser.add_argument("-m", "--motif", type=str, required=False, help="Motif")

if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)

args = parser.parse_args()

# converting input seq to uppercase
args.seq = args.seq.upper()

# check if seq has only ACTGU
if re.search('^[ACGTU]+$', args.seq):
	# seq with both T and U cannot be DNA or RNA
    if re.search('T', args.seq) and re.search('U', args.seq):
        print('The sequence is not DNA nor RNA')
	# seq with T is DNA
    elif re.search('T', args.seq):
        print('The sequence is DNA')
	# seq with U is RNA
    elif re.search('U', args.seq):
        print('The sequence is RNA')
	# seq without T or U can be either
    else:
        print('The sequence can be DNA or RNA')
# if none of the above, not DNA or RNA
else:
    print('The sequence is not DNA nor RNA')
# motif search within seq
if args.motif:
    args.motif = args.motif.upper()
    print(f'Motif search enabled: looking for motif "{args.motif}" in sequence "{args.seq}"... ', end='')

    if re.search(args.motif, args.seq):
        print("FOUND")
    else:
        print("NOT FOUND")
