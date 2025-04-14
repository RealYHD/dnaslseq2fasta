import re

from dnaslseq2fasta.structures import dnasl

def read_dnasl_seq(path: str):
    with open(path, "r") as file:
        name_match = re.match(r'"(.+)"', file.readline())
        if name_match is None:
            raise ValueError(f"{path} is not recognized as a DNAStar LaserGene sequence file. Missing contig name.")
        name = name_match.group(1)

        last_line = file.readline()
        while last_line != "^^\n" and last_line != "":
            last_line = file.readline()
        
        if last_line != "":
            sequence = file.readline()
        else:
            raise ValueError(f"{path} is not recognized as a DNAStar LaserGene sequence file. Missing consensus sequnece.")
        return dnasl.Sequence(name, sequence)
