"""File    : intersection_of_gene_names.py
 This program finds all gene symbols that appear both in the chr21_genes.txt file and in the HUGO_genes.txt file.
 These gene symbols are printed to a file in alphabetical order in the output file OUTPUT/intersection_output.txt)
  The program also prints on the terminal how many common gene symbols were found"""

import argparse
from assignment4.io_utils import get_filehandle


def main():
    """ Business Logic """

    args = get_cli_args()
    infile1 = args.infile1
    infile2 = args.infile2
    outfile = "OUTPUT/intersection_output.txt"

    # Using get_filehandle() for two input files and one output file

    fh_in1 = get_filehandle(infile1, "r")
    fh_in2 = get_filehandle(infile2, "r")
    fh_out = get_filehandle(file=outfile, mode="w")
    find_unique_gene_symbols(fh_in1, fh_in2, fh_out)


def get_gene_symbol(line):
    """ getting gene symbol list from both chr21_genes.txt file and HUGO_genes.txt file """
    line = line.strip()
    line = line.split("\t")[0]
    return line


def find_unique_gene_symbols(fh_in1, fh_in2, fh_out):
    """ finds unique gene symbols from both the text files. Intersection between two unique sets and sorted"""
    gene_set = set()
    hugo_set = set()

    for line in fh_in1:
        gene = get_gene_symbol(line)
        gene_set.add(gene)
    # print(gene_set)

    for line in fh_in2:
        gene = get_gene_symbol(line)
        hugo_set.add(gene)

    output_set = gene_set.intersection(hugo_set)
    output_set = sorted(output_set)
    # print(output_set)

    for gene in output_set:
        fh_out.write(gene + "\n")

    print("Number of unique gene names in chr21_genes.txt: " + str(len(gene_set)))
    print("Number of unique gene names in HUGO_genes.txt: " + str(len(hugo_set)))
    print("Number of common gene symbols found: " + str(len(output_set)))
    print("Output stored in OUTPUT/intersection_output.txt")


def get_cli_args():
    """
    CLI options using Python's argparse
    @return: Instance of argparse arguments
    """

    parser = argparse.ArgumentParser(description='Provide two gene list (ignore header line), find intersection')

    parser.add_argument('-i1', '--infile1', dest='infile1',
                        type=str, help='Path to file to open', required=True)
    parser.add_argument('-i2', '--infile2', dest='infile2',
                        type=str, help='Path to file to open', required=True)

    return parser.parse_args()


if __name__ == '__main__':
    main()
