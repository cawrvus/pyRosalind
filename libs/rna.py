from functools import reduce
from libs.nucl import NucleicAcid
from libs.const import RNA_NUCLEOTIDES
from libs.const import RNA_COMPLEMENTS


class RNA(NucleicAcid):
    def __init__(self, string, label=None):
        super().__init__(RNA.validated(string), label)

    @staticmethod
    def validated(string):
        raw = (c in RNA_NUCLEOTIDES for c in string)
        valid = reduce(lambda x, y: x and y, raw)
        if not valid:
            raise ValueError("Invalid nucleotides provided")
        return string

    @staticmethod
    def inverse(ncl):
        return RNA_COMPLEMENTS[ncl]

    @staticmethod
    def convert(string):
        return string.replace('T', 'U')
