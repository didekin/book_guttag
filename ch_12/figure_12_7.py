class IntDict(object):
    """A dictionary with integer keys"""

    def __init__(self, num_buckets):
        """create an empty dictionary"""
        self._buckets = []
        self._num_buckets = num_buckets
        for i in range(num_buckets):
            self._buckets.append([])

    def add_entry(self, key, dict_val):
        """Assumes key an int. Adds an entry."""
        hash_bucket = self._buckets[key % self._num_buckets]
        for i in range(len(hash_bucket)):
            if hash_bucket[i][0] == key:
                hash_bucket[i] = (key, dict_val)
                return
        hash_bucket.append((key, dict_val))

    def get_value(self, key):
        """Assumes key an int.
        Returns value associated with key"""
        hash_bucket = self._buckets[key % self._num_buckets]
        for e in hash_bucket:
            if e[0] == key:
                return e[1]
        return None

    def __str__(self):
        result = '{'
        for b in self._buckets:
            for e in b:
                result += str(e[0]) + ':' + str(e[1]) + ','
        return result[:-1] + '}'  # omits the last comma


bucket1 = IntDict(21)
bucket1.add_entry(123, 'Nevado')
bucket1.add_entry(113, 'Raja')
bucket1.add_entry(39, 'Pedro')
print(bucket1)
