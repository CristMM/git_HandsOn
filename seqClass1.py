#!/usr/bin/env python

import sys
from argparse import ArgumentParser

parser = ArgumentParser(description='Classify a sequence as DNA or RNA')
parser.add_argument("-s", "--seq", type=str, required=True, help="Input sequence")
parser.add_argument("-m", "--motif", type=str, required=False, help="Motif")

if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)

args = parser.parse_args()

args.seq = args.seq.upper()  # Convert the sequence to uppercase for comparison

# Define the sets of valid nucleotide bases
dna_bases = {'A', 'C', 'G', 'T', 'R', 'Y', 'S', 'W', 'K', 'M', 'B', 'D', 'H', 'V', 'N'}
rna_bases = {'A', 'C', 'G', 'U', 'R', 'Y', 'S', 'W', 'K', 'M', 'B', 'D', 'H', 'V', 'N'}

# Sequence classification
if set(args.seq).issubset(dna_bases):
    if 'U' in args.seq:
        print('The sequence is RNA')
    else:
        print('The sequence is DNA')
elif set(args.seq).issubset(rna_bases):
    if 'T' in args.seq:
        print('The sequence is DNA')
    else:
        print('The sequence is RNA')
else:
    print('The sequence is not valid as DNA or RNA')
    sys.exit(1)  # Exit if the sequence is invalid

# Motif search if provided
if args.motif:
    args.motif = args.motif.upper()
    print(f'Motif search enabled: looking for motif "{args.motif}" in sequence "{args.seq}"... ', end='')
    if args.motif in args.seq:
        print("FOUND")
    else:
        print("NOT FOUND")
