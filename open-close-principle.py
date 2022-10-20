# In the open/closed principle classes should be open for extension, but closed for modification.
# Essentially meaning that classes should be extended to change functionality, rather than being altered into something else.

#  In doing so, we stop ourselves from modifying existing code and causing potential new bugs in an otherwise happy application.
# Of course, the one exception to the rule is when fixing bugs in existing code.

# When business requirements change and we need to add or alter the existing functionality
# New methods and behaviours can be extended to it, but it cannot be modified.

# Other classes depend on the existing functionality and I change it, I may introduce bugs somewhere where I don't even know.

# The purpose of the open-closed principle is to make it easy to add new features
# (or use cases) to the system without directly modifying the existing code.

# EXAMPLE 1

class Person:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'Person(name={self.name})'


class PersonStorage:
    def save_to_database(self, person):
        print(f'Save the {person} to database')

    def save_to_json(self, person):
        print(f'Save the {person} to a JSON file')


if __name__ == '__main__':
    person = Person('John Doe')
    storage = PersonStorage()
    storage.save_to_database(person)

# In this example, the PersonStorage class has two methods:

# The save_to_database() method saves a person to the database.
# The save_to_json() method saves a person to a JSON file.
# Later, if you want to save the Person’s object into an XML file, you must modify the PersonStorage class.
# It means that the PersonStorage class is not open for extension but modification. Hence, it violates the open-closed principle.

# SOLUTION

from abc import ABC, abstractmethod

class Person:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'Person(name={self.name})'


class PersonStorage(ABC):
    @abstractmethod
    def save(self, person):
        pass


class PersonDB(PersonStorage):
    def save(self, person):
        print(f'Save the {person} to database')


class PersonJSON(PersonStorage):
    def save(self, person):
        print(f'Save the {person} to a JSON file')


class PersonXML(PersonStorage):
    def save(self, person):
        print(f'Save the {person} to a XML file')


if __name__ == '__main__':
    person = Person('John Doe')
    storage = PersonXML()
    storage.save(person)


# First, define the PersonStorage abstract class that contains the save() abstract method
# Second, create two classes PersonDB and PersonJSON that save the
# Person object into the database and JSON file. These classes inherit from the PersonStorage class
# Now you can define a new class PersonXML that inherits from the PersonStorage