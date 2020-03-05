class NucleicAcid:
    def __init__(self, string, label=None):
        self._string = string
        self._label = label

    @property
    def string(self):
        return self._string

    @property
    def label(self):
        return self._label

    def __str__(self):
        return self.string

    def __iter__(self):
        return (c for c in self.string)

    def __len__(self):
        return len(self.string)

    def __reversed__(self):
        return (c for c in reversed(self.string))
