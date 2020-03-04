from libs.seq import fib


class Population:
    def __init__(self, limit, litter=1, init=1):
        self.limit = limit
        self.litter = litter
        self.init = init

    @property
    def init(self):
        return self._init

    @init.setter
    def init(self, init):
        if Population.validate(init=init):
            self._init = init
        else:
            raise ValueError("Invalid intial number of pairs")

    @property
    def litter(self):
        return self._litter

    @litter.setter
    def litter(self, litter):
        if Population.validate(litter=litter):
            self._litter = litter
        else:
            raise ValueError("Invalid litter size")

    @property
    def limit(self):
        return self._limit

    @limit.setter
    def limit(self, limit):
        if Population.validate(limit=limit):
            self._limit = limit
        else:
            raise ValueError("Invalid limit")

    @staticmethod
    def validate(init=1, litter=1, limit=0):
        return init >= 0 and litter >= 0 and limit >= 0

    def fib_evolution(self):
        return fib(self.limit, self.litter) * self.init

    def fib_regression(self):
        pass
