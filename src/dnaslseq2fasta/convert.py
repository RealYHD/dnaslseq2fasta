from dnaslseq2fasta.structures import dnasl, sequences


def dnaslseq2general(dnaslseq: dnasl.Sequence):
    return sequences.NamedString(dnaslseq.name, dnaslseq.consensus)