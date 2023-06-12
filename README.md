# Dana-Farber-Coding-Assessment

## Author 

Tarishi Pathak

## Directory Structure

<img width="308" alt="Screenshot 2023-06-12 at 10 01 24 AM" src="https://github.com/tariship/Dana-Farber-Coding-Assessment/assets/90934721/1564db09-26e4-4574-8be2-f18a12572c52">


## Task 1

1. This program finds all FASTQ files in a given directory, recursively, and then returns the file name and the respective percentage of sequences in the file with more than 30 nucleotides.

__Example command__

```
./task1_fastq.py --directory "sample_files"
```

2. This program finds the 10 most frequent sequences in a FASTA file and returns the sequence and the number of times it occurs in the file.

__Example command__

```
./task1_fasta.py --input sample_files/fasta/sample.fasta
```

3. This program returns gene names for multiple chromosome and coordinates and outputs an annotated file (annotated_coordinates.csv) with the chromosome, coordinate and the respective gene name.

__Example command__

```
./task1_annotation.py --annotation_file sample_files/gtf/hg19_annotations.gtf --coordinates sample_files/annotate/coordinates_to_annotate.txt
```

## Task 2

This program parses a text file with information on coverage on exon level in a hybrid capture panel, bins the GC column in 10% intervals, and then reports the mean target coverage for the intervals grouped by GC% bins.

__Example command__

```
./task2.py --input_file Example.hs_intervals.txt
```

## Cloud Computing

1. Primarily, building a framework on a cloud platform where multiple users have access to the same file would require defining IAM roles and and managing permissions to access the shared files. For instance, AWS IAM allows defining access permissions for users and groups. To build on that, an authentication method such as MFA could be used to add a layer of security around file sharing as well as verify the user's permission level.

    Another aspect to consider would be to use a storage service such as AWS S3, which ensures that multiple users can have access to files by defining access permissions for the resources as well as the users to access those resources and actions.


2. 
__Benefits:__
- Containers provide consistency because they encapsulate programs and dependencies, which allows them to be ported across most environments. This enhances reproducibility of data and results
- They help support CI/CD because of consistency and easy deployment, enabling support for bioinformaticians to package applications as they code.
- They're scalable based on the computational needs, making them ideal for large genomics datasets and bionformatics pipelines.

__Limitations:__
- Large image sizes can take up a lot of space, and optimizing as well as maintaining image sizes can be demanding.
- Running a lot of containers at the same time can add pressure to the system's resources, which can lead to decreased performance.

## SQL

'GROUPBY(OrderID)' is missing.

So, the corrected statement would be:

```
SELECT UserId, AVG(Total) AS AvgOrderTotal 
FROM Invoices
GROUP BY UserId
HAVING COUNT(OrderId) >= 1
```
