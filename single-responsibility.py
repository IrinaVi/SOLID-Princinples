# Single reposibility principle
# a class should have a single responsibility
# a class should only have one reason to change

# From Uncle Bob's book:
# Any module (set of functions, class, source code, package) - should be changed only by one actor

# BENEFITS:
#
# Testing – A class with one responsibility will have far fewer test cases.
# Lower coupling – Less functionality in a single class will have fewer dependencies.
# Organization – Smaller, well-organized classes are easier to search than monolithic ones.

# EXAMPLE 1
#Three different stakeholders use this class:
class Employee:
    #CFO
    def calculate_salary(self):
        __get_regular_hours()

    #HR
    def calculate_hours(self):
        __get_regular_hours()
    #IT
    def save_emp_data(self):

    def __get_regular_hours(self):

# If CFO needs to change the calculate salary method, it may require the change in how the regular hours are calculated
# If this change is made that will affect the calculate hours function too.
# Now the HR will see the wrong data because the private method that is used  by both functions was changed
# Three different public methods of one class corresponded to different actors of the software
# The requirements for change should come only from one stakeholder or a business requirement
# Solution

class Calculate_salary:

class Calulate_hours

class Save_data:


# EXAMPLE 2

class Page():
    def __init__(self, title):
        self._title = title

    def get_title(self):
        return self._title

    def set_title(self, title):
        self._title = title

    def get_page(self):
        return [self._title]

    # returns page in json string
    def format_json(self):
        return json.dumps(self.get_page())

# What happens, however, if we want to change the output of the JSON string, or to add another type of output to the class?
# We would need to alter the class to either add another method or change an existing method to suit.

# SOLUTION

class Page():
    def __init__(self, title):
        self._title = title

    def get_title(self):
        return self._title

    def set_title(self, title):
        self._title = title

    def get_page(self):
        return [self._title]

class JsonPageFormatter():
    def format_json(page: Page):
        return json.dumps(page.get_page())
