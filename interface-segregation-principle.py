# This states that many client-specific interfaces are better than one general-purpose interface.
# In other words, classes should not be forced to implement interfaces they do not use.
#
# Let's take an example of a Worker interface. This defines several different methods that can be applied
# to a worker at a typical development agency.
# Interface is a set of methods an object must-have. The purpose of interfaces is to allow clients to request
# the correct methods of an object via its interface.

# The interface segregation principle states that an interface should be as small a possible in terms of cohesion.
# In other words, it should do ONE thing.
# It doesn’t mean that the interface should have one method. An interface can have multiple cohesive methods.

# EXAMPLE

from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def fly(self):
        pass

class Aircraft(Vehicle):
    def go(self):
        print("Taxiing")

    def fly(self):
        print("Flying")

class Car(Vehicle):
    def go(self):
        print("Going")

    def fly(self):
        raise Exception('The car cannot fly')

# In this design the Car class must implement the fly() method from the Vehicle class that the Car class doesn’t use.
# Therefore, this design violates the interface segregation principle.

# SOLUTION

class Movable(ABC):
    @abstractmethod
    def go(self):
        pass


class Flyable(Movable):
    @abstractmethod
    def fly(self):
        pass

class Aircraft(Flyable):
    def go(self):
        print("Taxiing")

    def fly(self):
        print("Flying")

class Car(Movable):
    def go(self):
        print("Going")