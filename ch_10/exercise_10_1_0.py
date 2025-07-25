class IntSet(object):
    """An Int_set is a set of integers"""

    # Information about the implementation (not the abstraction):
    # value of a set is represented by a list of ints, self._vals.
    # Each int in a set occurs exactly once.

    def __init__(self):
        """create an empty set of integers"""
        self._vals = []

    def insert(self, e):
        """Assumes e is an integer and inserts e into self"""
        if e not in self._vals:
            self._vals.append(e)

    def member(self, e):
        """Assumes e is an integer
        Returns True if e is in self, and False otherwise"""
        return e in self._vals

    def remove(self, e):
        """Assumes e is an integer and removes e from self
        Raises ValueError if e is not in self"""
        try:
            self._vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')

    def get_members(self):
        """Returns a list containing the elements of self.
        Nothing can be assumed about the order of the elements"""
        return self._vals[:]

    def union(self, other):
        """other is an IntSet. Mutates self so that it contains exactly the elemnts in self
           plus the elements in other."""
        for el in other.get_members():
            self.insert(el)

    def __str__(self):
        """Returns a string representation of self"""
        if not self._vals:
            return '[]'
        self._vals.sort()
        result = ''
        for e in self._vals:
            result = result + str(e) + ','
        return '[' + result[:-1] + ']'


xx = IntSet()
xx.insert(1)
yy = IntSet()
yy.insert(2)
yy.insert(1)
yy.insert(3)
xx.union(yy)
print(xx)
