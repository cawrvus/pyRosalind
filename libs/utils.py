def char_count(string, char):
    return len([c for c in string if c == char])


def from_file(file, delimiter=None):
    with open(file, "r") as fd:
        return fd.read().strip().split(delimiter)


def to_file(ls, file, delimiter=''):
    with open(file, "w") as fd:
        fd.write(delimiter.join(list(map(str, ls))))
