#!/usr/bin/env python3

from pathlib import Path
import os
import argparse

parser = argparse.ArgumentParser(description='Recursively finds FASTQ files in a directory and returns the file name and the percent of sequences longer than 30 nucleotides')
parser.add_argument('--directory', default = "sample_files", help="Input directory path")
args = parser.parse_args()

def nucleotide_percent_calculation(file_path):

    # parse FASTQ file and make a list of sequences
    with open(file_path, 'r') as f:
        line_list = f.readlines()
    seq_list = line_list[1::4]
    seq_list = [i.strip() for i in seq_list]

    # count sequences with more than 30 nucleotides
    target_seq_count = 0
    for seq in seq_list:
        if len(seq)  > 30:
            target_seq_count += 1

    total_seq_count = len(seq_list)

    return (target_seq_count/total_seq_count) * 100


# recursively find FASTQ in given directory
for files in Path(args.directory).rglob("*.fastq"):
    file_path = os.path.join(str(files.parent.absolute()) + "/" + str(files.name))
    print(files.name, nucleotide_percent_calculation(file_path))


