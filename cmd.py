from libs.dna import DNA
from libs.rna import RNA
from libs.gen import Genotypes
from libs.popul import Population


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


def rev_comp(_obj):
    return _obj.rev_complement()


def gen_comb(_ls, _type):
    return [Genotypes.combine(*_ls, _type)]


def gen(_ls):
    dom, het, rec = list(int(i) for i in _ls)
    return Genotypes.create(dom, het, rec)


def popul(_ls):
    return Population(*_ls)


def evolve(_pop):
    return [_pop.fib_evolution()]
