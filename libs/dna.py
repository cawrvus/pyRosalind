from functools import reduce
from libs.nucl import NucleicAcid
from libs.const import DNA_NUCLEOTIDES
from libs.const import DNA_COMPLEMENTS


class DNA(NucleicAcid):
    def __init__(self, string, label=None):
        super().__init__(DNA.validated(string), label)

    @staticmethod
    def validated(string):
        raw = (c in DNA_NUCLEOTIDES for c in string)
        valid = reduce(lambda x, y: x and y, raw)
        if not valid:
            raise ValueError("Invalid nucleotides provided")
        return string

    @staticmethod
    def inverse(ncl):
        return DNA_COMPLEMENTS[ncl]

    @staticmethod
    def convert(string):
        return string.replace('U', 'T')
