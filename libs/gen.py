from functools import reduce
from enum import Enum
from libs.comb import binom


class Allele(Enum):
    DOMINANT = 1
    RECESSIVE = 0


class Genotypes:
    @staticmethod
    def combine(dom, het, rec, a_type):
        count = len(dom + het + rec)
        total = 2 * count
        rec_count = len(rec)
        rec_total = rec_count * 2 + len(het)

        combinations = binom(total, 2) - count
        recessives = binom(rec_total, 2) - rec_count
        dominants = combinations - recessives

        probability = recessives / combinations, dominants / combinations

        return probability[a_type.value]

    @staticmethod
    def create(dom, het, rec):
        dominant = list(Genotype((1, 1)) for _ in range(dom))
        hetero = list(Genotype((1, 0)) for _ in range(het))
        recessive = list(Genotype((0, 0)) for _ in range(rec))

        return dominant, hetero, recessive


class Genotype:
    def __init__(self, geno):
        self._geno = Genotype.validated(geno)

    @property
    def geno(self):
        return self._geno

    @staticmethod
    def validated(geno):
        raw = (a in set(i.value for i in Allele) for a in geno)
        valid = reduce(lambda x, y: x and y, raw) and len(geno) == 2
        if not valid:
            raise ValueError("Invalid genotype provided")
        return geno
