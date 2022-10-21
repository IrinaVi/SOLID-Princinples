# Created by Barbara Liskov in a 1987, this states that objects should be replaceable
# by their subtypes without altering how the program works.
# In other words, derived classes must be substitutable for their base classes without causing errors.

# EXAMPLE 1

class Rectangle():
    def __init__(self, width, height):
        self._width = width
        self._height = height

    def get_width(self):
        return self._width

    def set_width(self, width):
        self._width = width

    def get_height(self):
        return self._height

    def set_height(self, height):
        self._height = height

    def area(self):
        return self.get_width() * self.get_height()

class Square(Rectangle):
    def __init__(self, width):
        self._width = width
        self._height = width

    def get_width(self):
        return self._width

    def set_width(self, width):
        self._width = width
        self._height = width

    def get_height(self):
        return self._height

    def set_height(self, height):
        self._height = height
        self._width = height

# EXAMPLE 2

from abc import ABC, abstractmethod

class Notification(ABC):
    @abstractmethod
    def notify(self, message, email):
        pass


class Email(Notification):
    def notify(self, message, email):
        print(f'Send {message} to {email}')


class SMS(Notification):
    def notify(self, message, phone):
        print(f'Send {message} to {phone}')


if __name__ == '__main__':
    notification = SMS()
    notification.notify('Hello', 'john@test.com')

# The notify() method of the Email class sends a message to an email, which is fine.
#
# However, the SMS class uses a phone number, not an email, for sending a message. Therefore, we need to change
# the signature of the notify() method of the SMS class to accept a phone number instead of an email.

# The following NotificationManager class uses the Notification object to send a message to a Contact:

class Contact:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone


class NotificationManager:
    def __init__(self, notification, contact):
        self.contact = contact
        self.notification = notification

    def send(self, message):
        if isinstance(self.notification, Email):
            self.notification.notify(message, contact.email)
        elif isinstance(self.notification, SMS):
            self.notification.notify(message, contact.phone)
        else:
            raise Exception('The notification is not supported')


if __name__ == '__main__':
    contact = Contact('John Doe', 'john@test.com', '(408)-888-9999')
    notification_manager = NotificationManager(SMS(), contact)
    notification_manager.send('Hello John')


# SOLUTION
# First, redefine the notify() method of the Notification class so that it doesn’t include the email parameter:

class Notification(ABC):
    @abstractmethod
    def notify(self, message):
        pass

# Second, add the email parameter to the __init__ method of the Email class:

class Email(Notification):
    def __init__(self, email):
        self.email = email

    def notify(self, message):
        print(f'Send "{message}" to {self.email}')

# Third, add the phone parameter to the __init__ method of the SMS class:

class SMS(Notification):
    def __init__(self, phone):
        self.phone = phone

    def notify(self, message):
        print(f'Send "{message}" to {self.phone}')

# Fourth, change the NotificationManager class:

class NotificationManager:
    def __init__(self, notification):
        self.notification = notification

    def send(self, message):
        self.notification.notify(message)
