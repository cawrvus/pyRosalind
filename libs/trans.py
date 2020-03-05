from functools import reduce


def matches(_iter, _match):
    return list(list(_iter).count(c) for c in _match)


def count(_iter):
    return len(_iter)


def rev_complement(_iter):
    raw = (_iter.inverse(n) for n in reversed(_iter))
    return reduce(lambda x, y: x + y, raw)


def combine(_objs, _ls, _filter):
    return [_objs.combine(*_ls, _filter)]


def evolve(_obj, _seq_fn):
    return [_obj.evolve(_seq_fn)]


def convert(_from, _to):
    return _to.convert(str(_from))


def cast(_from, _to):
    return _to(_to.convert(_from))
