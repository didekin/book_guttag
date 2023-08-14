class IntSet(object):

    def __init__(self):
        self._vals = []

    def add_list(self, listin):
        for j in listin:
            self.insert(j)
        return self

    def insert(self, e):
        if e not in self._vals:
            self._vals.append(e)

    def get_members(self):
        return self._vals[:]

    # noinspection GrazieInspection
    def union(self, other):
        """other is an IntSet
           mutates self so that it contains exactly the elemnts in self plus the elements in other.
        """
        for j in other.get_members():
            self.insert(j)
        return self


L1 = [1, 2, 3, 8]
L2 = [8, 9]
s1 = IntSet().add_list(L1)
s2 = IntSet().add_list(L2)
print(s1.get_members())
print(s2.get_members())
print(s1.union(s2).get_members())
