from functools import reduce
from libs.utils import char_count


class RNA:
    nucleotides = ['A', 'C', 'G', 'U']

    def __init__(self, string):
        self.string = string

    def __str__(self):
        return self.string

    @property
    def string(self):
        return self._string

    @string.setter
    def string(self, string):
        if RNA.validate(string):
            self._string = string
        else:
            raise ValueError("Invalid nucleotides provided")

    @staticmethod
    def validate(string):
        valid = [c in RNA.nucleotides for c in string]
        result = reduce(lambda x, y: x and y, valid)
        return result

    @staticmethod
    def nucleic_inverse(ncl):
        return {'A': 'U', 'U': 'A', 'C': 'G', 'G': 'C'}[ncl]

    def count(self):
        return [char_count(self.string, n) for n in RNA.nucleotides]

    def to_dna(self):
        return self.string.replace('U', 'T')

    def complement(self):
        return [self.nucleic_inverse(n) for n in reversed(self.string)]
