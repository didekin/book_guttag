# noinspection PyBroadException

import datetime


class Person(object):
    # noinspection PyBroadException
    def __init__(self, name):
        """Assumes name a string. Create a person"""
        self._name = name
        try:
            last_blank = name.rindex(' ')
            self._last_name = name[last_blank + 1:]
        except:
            self._last_name = name
            self._birthday = None

    def get_name(self):
        """Returns self's full name"""
        return self._name

    def get_last_name(self):
        """Returns self's last name"""
        return self._last_name

    def set_birthday(self, birthdate):
        """Assumes birthdate is of type datetime.date
        Sets self's birthday to birthdate"""
        self._birthday = birthdate

    def get_age(self):
        """Returns self's current age in days"""
        if self._birthday is None:
            raise ValueError
        return (datetime.date.today() - self._birthday).days

    # noinspection PyProtectedMember
    def __lt__(self, other):
        """Assume other a Person.
        Returns True if self precedes other in alphabetical
        order, and False otherwise. Comparison is based on last
        names, but if these are the same full names are
        compared."""
        if self._last_name == other._last_name:
            return self._name < other._name
        return self._last_name < other._last_name

    def __str__(self):
        """Returns self's name"""
        return self._name


class Politician(Person):
    """ A politician is a person who can belong to a political party"""

    def __init__(self, name, party=None):
        """name and party are strings"""
        super().__init__(name)
        self._party = party

    def get_party(self):
        """returns the party to which self belongs"""
        return self._party

    def might_agree(self, other):
        """returns True if self and other belong to the same or at least one of then does not belong to a party """
        return self._party == other.get_party() or (self._party is None or other.get_party() is None)


person1 = Person('Person1 Name1')
person2 = Person('Person2 Name2')
person3 = Person('Person3 Name3')
person4 = Person('Person4 Name4')
politician1 = Politician(person1.get_name(), 'Party1')
politician2 = Politician(person2.get_name(), 'Party2')
politician3 = Politician(person3.get_name())
politician4 = Politician(person4.get_name(), 'Party1')
print(politician1.might_agree(politician2))
print(politician1.might_agree(politician3))
print(politician1.might_agree(politician4))