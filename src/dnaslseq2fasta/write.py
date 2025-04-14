
from dnaslseq2fasta.structures import sequences


def general2fasta(path: str, general_seq: sequences.NamedString):
    header_template = f">{general_seq.name}|{general_seq.name}|{general_seq.name} Unknown OS=Unknown OX=Unknown [GN=Unknown ]PE=Unknown SV=0"
    with open(path, "w") as file:
        file.write(header_template)
        file.write("\n")
        file.write(general_seq.sequence)