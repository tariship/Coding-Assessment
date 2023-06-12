#!/usr/bin/env python3

import argparse

parser = argparse.ArgumentParser(description='Finds the 10 most frequent sequences in a FASTA file and the number of times they appear.')
parser.add_argument('--input_file', default = "sample_files/fasta/sample.fasta", help="Input FASTA file")
args = parser.parse_args()

seq_freq = {}

# parse FASTA file and make a list of sequences
with open(args.input_file, 'r') as f:
    line_list = f.readlines()
seq_list = line_list[1::2]
seq_list = [i.strip() for i in seq_list]

# count occurence of each sequence
for seq in seq_list:
    seq_freq[seq] = seq_list.count(seq)

# sort by highest to lowest frequency
sorted_freq = sorted(seq_freq.items(), key = lambda x:x[1], reverse = True)

# extract 10 most frequent sequences
top_10_freq = sorted_freq[:10]

for i,j in top_10_freq:
    print(i,j)
