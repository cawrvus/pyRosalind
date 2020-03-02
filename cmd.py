from libs.dna import DNA
from libs.rna import RNA
from libs.gen import Genotypes


def count(_obj):
    return _obj.count()


def dna(_ls):
    return DNA(*_ls)


def rna(_ls):
    return RNA(*_ls)


def dna2rna(_dna):
    return _dna.to_rna()


def rna2dna(_rna):
    return _rna.to_dna()


def cast2rna(_dna):
    return RNA(dna2rna(_dna))


def cast2dna(_rna):
    return DNA(rna2dna(_rna))


def complement(_obj):
    return _obj.complement()


def gen_combine(_ls, _type):
    return [Genotypes.combine(*_ls, _type)]


def gen_create(_ls):
    dom, het, rec = [int(i) for i in _ls]
    return Genotypes.create(dom, het, rec)
