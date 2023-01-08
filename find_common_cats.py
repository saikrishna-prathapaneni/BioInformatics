"""
File    : find_common_cats.py
 This program counts how many genes are in each category based on data from the chr21_genes.txt file and
  the program print the results of the categories that are arranged in ascending order to an output file"""

import argparse
from assignment4.io_utils import get_filehandle
import collections


def main():
    """ Business Logic """

    args = get_cli_args()
    infile1 = args.infile1
    infile2 = args.infile2
    outfile = "OUTPUT/categories.txt"

    # Using get_filehandle() for two input files and one output file
    fh_in1 = get_filehandle(infile1, "r")
    fh_in2 = get_filehandle(infile2, "r")
    fh_out = get_filehandle(file=outfile, mode="w")
    counts = gene_count(fh_in1)
    d = store_the_description(fh_in2)
    result(fh_out, counts, d)


def gene_count(fh_in1):
    """ creating dictionary to stores the category and counts how many genes are in each category in ascending order"""
    counts = {}
    fh_in1.readline()

    while True:
        line = fh_in1.readline()
        if line == '':
            break
        line = line.split('\t')
        try:
            counts[line[0]] = line[2]
            counts[line[0]] = line[2].strip()
        except:
            pass
    count = collections.Counter(counts.values())

    # print(count)

    sorted_dict = dict(sorted(count.items(), key=lambda x: x[0]))
    # print(sorted_dict)
    # print('count', count)
    return sorted_dict


def store_the_description(fh_in2):
    """ creating dictionary to store the description from the file chr21_genes_categories.txt"""
    line = fh_in2.readlines()
    d = {}
    for lines in line:
        # print(lines.split("    "))
        category = lines.split("    ")[0].strip()
        description = lines.split("    ")[1].strip()
        d[category] = description
    return d


def result(fh_out, counts, d):
    fh_out.write("Category\tOccurrence\tDescription\n")

    for key1, value1 in counts.items():
        for key2, value2 in d.items():
            if key1 == key2:
                fh_out.write(f'{key1}\t{value1}\t{value2}\n')


def get_cli_args():
    """
     CLI options using Python's argparse
     @return: Instance of argparse arguments
     """

    parser = argparse.ArgumentParser(description='Combine on gene name and count the category occurrence ')

    parser.add_argument('-i1', '--infile1', dest='infile1',
                        type=str, help='Path to file to open', required=True)
    parser.add_argument('-i2', '--infile2', dest='infile2',
                        type=str, help='Path to file to open', required=True)

    return parser.parse_args()


if __name__ == '__main__':
    main()
