class Population:
    def __init__(self, limit, litter=1, init=1):
        self._limit = Population.validated(limit=limit)
        self._litter = Population.validated(litter=litter)
        self._init = Population.validated(init)

    @property
    def init(self):
        return self._init

    @property
    def litter(self):
        return self._litter

    @property
    def limit(self):
        return self._limit

    @staticmethod
    def validated(init=1, litter=1, limit=0):
        return init >= 0 and litter >= 0 and limit >= 0

    def evolve(self, seq_fn):
        return seq_fn(self.limit, self.litter) * self.init

    def fib_regression(self):
        pass
