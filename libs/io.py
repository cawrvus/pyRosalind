def from_file(file, delimiter=None, fasta=False, cast=(lambda x: x)):
    with open(file, "r") as fd:
        return list(map(cast, fd.read().strip().split(delimiter)))


def to_file(ls, file, delimiter='', fasta=False):
    with open(file, "w") as fd:
        fd.write(delimiter.join(list(map(str, ls))))
