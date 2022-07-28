from itertools import product


def pad(n): return f'{n:>3}'  # noqa E731


class MultiplicationTable:

    def __init__(self, length):
        """Create a 2D self._table of (x, y) coordinates and
           their calculations (form of caching)"""
        self.length = length
        axis = range(1, self.length + 1)
        self._table = {(i, j): i*j
                       for i, j in product(axis, axis)}

    def __len__(self):
        """Returns the area of the table (len x* len y)"""
        return len(self._table)

    def __str__(self):
        """Returns a string representation of the table"""
        output = []
        for i, res in enumerate(self._table.values(), 1):
            val = str(res)
            val += i % self.length == 0 and '\n' or ' | '
            output.append(val)
        return ''.join(output)

    def calc_cell(self, x, y):
        """Takes x and y coords and returns the re-calculated result"""
        if not (x, y) in self._table:
            raise IndexError
        return x * y
