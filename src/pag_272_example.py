class IntDict(object):
    def __init__(self, numbuckets):
        self.buckets = []
        self.numbuckets = numbuckets
        for i in range(numbuckets):
            self.buckets.append([])

    def entry(self, key, dictval):
        hashbucket = self.buckets[key % self.numbuckets]
        for i in range(len(hashbucket)):
            if hashbucket[i][0] == key:
                # noinspection PyTypeChecker
                hashbucket[i] = (key, dictval)
                return
        # noinspection PyTypeChecker
        hashbucket.append((key, dictval))


dict10 = IntDict(10)
print(dict10.buckets)
dict10.entry(12, 'doce')
print(dict10.buckets)
dict10.entry(13, 'trece')
print(dict10.buckets)
dict10.entry(22, 'veintidos')
print(dict10.buckets)
