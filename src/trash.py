class IntSet(object):

    def __init__(self, elems):
        self._vals = elems

    def get_members(self):
        return self._vals[:]


L1 = [1, 2, 3, 8]
set1 = IntSet(L1)
print(set1.get_members())
