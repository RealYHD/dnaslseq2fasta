import argparse
from os import path
import os

from dnaslseq2fasta.convert import dnaslseq2general
from dnaslseq2fasta.read import read_dnasl_seq
from dnaslseq2fasta.write import general2fasta


def run():
    argparser = argparse.ArgumentParser()
    argparser.add_argument(
        "DNAS",
        action="extend",
        nargs="+",
        help="The DNAStar LaserGene .seq files to convert to FASTA."
    )
    argparser.add_argument(
        "output",
        help="The output folder."
    )
    args = argparser.parse_args()
    
    for dnas_file in args.DNAS:
        dnas_seq = read_dnasl_seq(dnas_file)
        general_seq_data = dnaslseq2general(dnas_seq)
        os.makedirs(path.abspath(args.output), exist_ok=True)
        general2fasta(path.join(path.abspath(args.output), path.basename(dnas_file)), general_seq_data)

def main():
    run()

if __name__ == "__main__":
    main()