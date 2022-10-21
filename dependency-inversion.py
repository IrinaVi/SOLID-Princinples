# High level modules or low level modules should not depend on the actual implementation.
# They should depend on abstractions.
# Implement abstractions using interfaces. Client classes should not depend on internal inmplementation of classes.
# instead, they should depend on abstraction.
#
# Problems if the principle is not respected:
# If one class depends on another, if the other class changes, then it will affect the other class
# Difficult to test

# EXAMPLE 1

class FXConverter:
    def convert(self, from_currency, to_currency, amount):
        print(f'{amount} {from_currency} = {amount * 1.2} {to_currency}')
        return amount * 1.2


class App:
    def start(self):
        converter = FXConverter()
        converter.convert('EUR', 'USD', 100)


if __name__ == '__main__':
    app = App()
    app.start()

# The FXConverter class uses an API from an imaginary FX third-party to convert an amount from one currency to another.
# For simplicity, we hardcoded the exchange rate as 1.2. In practice, you will need to make an API call to get
# the exchange rate.

# The App class has a start() method that uses an instance of the FXconverter class to convert 100 EUR to USD.
# The App is a high-level module. However, The App depends heavily on the FXConverter class that is dependent on
# the FX’s API.

# In the future, if the FX’s API changes, it’ll break the code. Also, if you want to use a different API, you’ll
# need to change the App class.

# To prevent this, you need to invert the dependency so that the FXConverter class needs to adapt to the App class.
#
# To do that, you define an interface and make the App dependent on it instead of FXConverter class.
# And then you change the FXConverter to comply with the interface.

# Solution

# First, define an abstract class CurrencyConverter that acts as an interface. The CurrencyConverter class
# has the convert() method that all of its subclasses must implement:

from abc import ABC

class CurrencyConverter(ABC):
    def convert(self, from_currency, to_currency, amount) -> float:
        pass

# Second, redefine the FXConverter class so that it inherits from the CurrencyConverter class and implement the
# convert() method:

class FXConverter(CurrencyConverter):
    def convert(self, from_currency, to_currency, amount) -> float:
        print('Converting currency using FX API')
        print(f'{amount} {from_currency} = {amount * 1.2} {to_currency}')
        return amount * 2

# Third, add the __init__ method to the App class and initialize the CurrencyConverter‘s object:

class App:
    def __init__(self, converter: CurrencyConverter):
        self.converter = converter

    def start(self):
        self.converter.convert('EUR', 'USD', 100)

# Now, the App class depends on the CurrencyConverter interface, not the FXConverter class.
# The following creates an instance of the FXConverter and pass it to the App:

if __name__ == '__main__':
    converter = FXConverter()
    app = App(converter)
    app.start()