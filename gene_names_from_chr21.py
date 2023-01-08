"""
File   : gene_names_from_chr21.py
This program  asks the user to enter a gene symbol, and then it prints the description for that gene based on data from
the chr21_genes.txt file.The program gives an error message if the entered symbol is not found and continues to ask the
user for genes until "quit" or "exit".

"""
import argparse
from assignment4.io_utils import get_filehandle


def reading_textfile_into_dict(fh_in):
    """
    creating a dictionary to store categories and gene discription
    :param fh_in:
    :return:
    """

    d = {}
    fh_in.readline()

    while True:
        line = fh_in.readline()
        if line == '':
            break
        line = line.split('\t')
        d[line[0]] = line[1]
    return d


def main():
    """ Business Logic """

    args = get_cli_args()
    infile1 = args.infile
    fh_in = get_filehandle(infile1, "r")
    description = reading_textfile_into_dict(fh_in)
    while True:
        gene = input("Enter gene name of interest. Type quit to exit:")
        if gene in description:
            print(f"{gene} found! Here is the description:")
            print(description[gene])
        elif gene == "quit":
            print("Thanks for querying the data.")
            break
        else:
            print("Not a valid gene name.")


def get_cli_args():
    """
     CLI options using Python's argparse
     @return: Instance of argparse arguments
     """

    parser = argparse.ArgumentParser(description='Open chr21_genes.txt, and ask user for a gene name')

    parser.add_argument('-i', '--infile', dest='infile',
                        type=str, help='Path to file to open', required=True)

    return parser.parse_args()


if __name__ == '__main__':
    main()
