from libs.dna import DNA
from libs.rna import RNA
from libs.gen import Genotypes
from libs.popul import Population


def dna(_ls):
    return DNA(*_ls)


def rna(_ls):
    return RNA(*_ls)


def gens(_ls):
    dom, het, rec = list(int(i) for i in _ls)
    return Genotypes.create(dom, het, rec)


def popul(_ls):
    return Population(*_ls)
