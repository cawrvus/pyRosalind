from re import fullmatch
from itertools import groupby
from functools import reduce


def from_file(file, delimiter=None, fasta=False, cast=(lambda x: x)):
    with open(file, "r") as fd:
        return list(map(cast, fd.read().strip().split(delimiter)))


def from_fasta(file):
    with open(file, "r") as fd:
        read = fd.readlines()
        grouped = groupby(read, lambda x: not fullmatch(">.*\n", x))
        groups = (list(v) for k, v in grouped)
        result = {i[0].strip(): reduce(lambda x, y: x.strip() + y.strip(), next(groups)) for i in groups}
        return result


def to_fasta(dct, file):
    with open(file, "w") as fd:
        lines = list(reduce(lambda x, y: x + y, dct.items()))
        fd.write('\n'.join(lines))


def to_file(ls, file, delimiter='', fasta=False):
    with open(file, "w") as fd:
        fd.write(delimiter.join(list(map(str, ls))))
