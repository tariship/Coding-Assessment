#!/usr/bin/env python3

import csv
import argparse

parser = argparse.ArgumentParser(description='Reports mean coverage for the intervals grouped by GC percent bins')
parser.add_argument('--input_file', default = "Example.hs_intervals.txt" , help="Input file containing information on covereage on exon level in a hybrid capture panel")
args = parser.parse_args()

bins = {}

# read text file
with open(args.input_file, 'r') as f:
    hc_interval = csv.reader(f, delimiter='\t')
    next(hc_interval) 

    for row in hc_interval:
        # convert GC to percentage 
        GC_value = float(row[5]) * 100  
        coverage = float(row[6])

        # bin GC column in 10% intervals
        bin_label = f'{int(GC_value // 10) * 10}-{int(GC_value // 10) * 10 + 10}'
        if bin_label not in bins:
            bins[bin_label] = []
        bins[bin_label].append(coverage)

# calculate mean target coverage for each interval
mean_target_coverage = {bin_label: sum(coverages) / len(coverages) for bin_label, coverages in bins.items()}

for bin_label, mean_coverage in mean_target_coverage.items():
    print(f'{bin_label}: {mean_coverage}')
