# 9-3: Users

# Make a class called User
class User:
    """A simple attempt to represent a User"""

    def __init__(self, first_name, last_name, age, date_joined):
        """Initialize attributes to describe a user"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.date_joined = date_joined

    def describe_user(self):
        """A description of the user."""
        print(f"\n{self.first_name} {self.last_name} is {self.age} years old and has been a user since {self.date_joined}.")

    def greet_user(self):
        """A personalized greeting to the user."""
        print(f"\nWelcome back, {self.first_name}!")


user_1 = User('Jeff', 'Whozit', 47, '10-28-2014')
user_2 = User('Lauren', 'Whatsit', 33, '07-05-2016')
user_3 = User('Wang', 'Wangerson', 31, '02-24-2017')

user_1.describe_user()
user_1.greet_user()

user_2.describe_user()
user_2.greet_user()

user_3.describe_user()
user_3.greet_user()
