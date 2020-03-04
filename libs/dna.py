from functools import reduce
from libs.utils import char_count


class DNA:
    nucleotides = ['A', 'C', 'G', 'T']

    def __init__(self, string, label=None):
        self.string = string
        self.label = label

    def __str__(self):
        return self.string

    @property
    def string(self):
        return self._string

    @string.setter
    def string(self, string):
        if DNA.validate(string):
            self._string = string
        else:
            raise ValueError("Invalid nucleotides provided")

    @property
    def label(self):
        return self._label

    @label.setter
    def label(self, label):
        self._label = label

    @staticmethod
    def validate(string):
        valid = (c in DNA.nucleotides for c in string)
        result = reduce(lambda x, y: x and y, valid)
        return result

    @staticmethod
    def nucleic_inverse(ncl):
        return {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}[ncl]

    def count(self):
        return list(char_count(self.string, n) for n in DNA.nucleotides)

    def to_rna(self):
        return self.string.replace('T', 'U')

    def rev_complement(self):
        raw = (DNA.nucleic_inverse(n) for n in reversed(self.string))
        return reduce(lambda x, y: x + y, raw)
