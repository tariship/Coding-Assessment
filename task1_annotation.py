#!/usr/bin/env python3

import csv
import argparse

parser = argparse.ArgumentParser(description='Looks up gene name for the chromosome and coordinate and writes it to a file.')
parser.add_argument('--annotation_file', default = "sample_files/gtf/hg19_annotations.gtf", help="Input GTF file with annotation information")
parser.add_argument('--coordinates', default = "sample_files/annotate/coordinates_to_annotate.txt", help="Input text file with coordinates to be annotated")
args = parser.parse_args()

def get_target_locations(coordinates_to_annotate):
    target_locations = {}

    # read text file with coordinates and chromosome
    with open(coordinates_to_annotate, 'r') as f:
        coordinates = csv.reader(f, delimiter='\t')
        for row in coordinates:
            chrom = row[0]
            location = int(row[1])
            target_locations[(chrom, location)] = None 
    return target_locations

def check_coord_overlaps(annotation_file, target_location_file):
    gene_names = {}
    results = []

    # read GTF with annotation information
    with open(annotation_file, 'r') as f:
        annotations = csv.reader(f, delimiter='\t')

        # extracting gene name from last column
        for row in annotations:
            gene_name = None
            for attribute in row[8].split(';'):
                if 'gene_name' in attribute:
                    gene_name = attribute.split('"')[1].strip()
                    break
            
            chrom = row[0]
            start = int(row[3])
            end = int(row[4])

            if gene_name:
                k = (chrom, start, end)
                gene_names[k] = gene_name

    target_locations = get_target_locations(target_location_file)

    # check if coordinate falls within the start, end region and return
    # respective gene name
    for (chrom, target) in target_locations.keys():
        for (region, start, end), gene_name in gene_names.items():
            if chrom == region and start <= target <= end:
                results.append((chrom, target, gene_name))
                break

    return results

chrom_coord_gene = check_coord_overlaps(args.annotation_file, args.coordinates)

# write the Chromosome, Coordinate and gene name to a CSV file
with open("annotated_coordinates.csv", 'w') as o:
        csv.writer(o).writerow(['Chrom', 'Coordinate', 'Gene name'])
        csv.writer(o).writerows(chrom_coord_gene)

        
