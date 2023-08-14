class Person(object):
    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self._name


class Politician(Person):
    """ A politician is a person who can belong to a
political party"""

    def __init__(self, name, party=None):
        """name and party are strings"""
        super().__init__(name)
        self._party = party

    def get_party(self):
        """returns the party to which self belongs"""
        return self._party

    def might_agree(self, other):
        """returns True if self and other belong to the same party
             or at least one of then does not belong to a party"""
        print(f'self: {self.get_party()}, other: {other.get_party()}')
        return ((self.get_party() == other.get_party()) or
                not (self.get_party() is not None and other.get_party() is not None))


P1 = Politician('David', 'RE')
P2 = Politician('John')
P3 = Politician('Curl', 'DE')
P4 = Politician('Lee', 'DE')
print(P1.might_agree(P2))
print(P1.might_agree(P3))
print(P3.might_agree(P4))
print(P2.might_agree(P3))
print(P4.might_agree(P2))

