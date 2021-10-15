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
        self.login_attempts = 0

    def describe_user(self):
        """A description of the user."""
        print(f"\n{self.first_name} {self.last_name} is {self.age} years old and has been a user since {self.date_joined}.")

    def greet_user(self):
        """A personalized greeting to the user."""
        print(f"\nWelcome back, {self.first_name}!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


user_1 = User('Jeff', 'Whozit', 47, '10-28-2014')
user_2 = User('Lauren', 'Whatsit', 33, '07-05-2016')
user_3 = User('Wang', 'Wangerson', 31, '02-24-2017')

user_1.describe_user()
user_1.greet_user()

user_2.describe_user()
user_2.greet_user()

user_3.describe_user()
user_3.greet_user()

# 9-5: Login Attempts
# Add an attribute called login_attempts to your User class. 
# Write a method to increment the value of login_attempts by 1
# Write another method that resets the value of login_attempts to 0
user_4 = User('Becky', 'Johnson', 28, '05-21-2015')
user_4.increment_login_attempts()
user_4.increment_login_attempts()
user_4.increment_login_attempts()
user_4.increment_login_attempts()
user_4.increment_login_attempts()
user_4.increment_login_attempts()
user_4.increment_login_attempts()
print("Login attempts: ", user_4.login_attempts)
user_4.reset_login_attempts()
print("Login attempts: ", user_4.login_attempts)

class Privileges:
    """A representation of user privileges"""

    def __init__(self):
        """Initialize attributes of privileges."""
        self.privileges = ['can delete post', 'can add post', 'can ban user', 'can demand candy']

    def show_privileges(self):
        """Print a list of privileges"""
        print(f"\nKnown Privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")

# 9-7: Admin
class Admin(User):
    """A special type of User, inheriting from the User class"""

    def __init__(self, first_name, last_name, age, date_joined):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an admin.
        """
        super().__init__(first_name, last_name, age, date_joined)
        self.wizardry_level = 5
        self.privileges = Privileges()


admin_user = Admin('Larry', 'Dog', 6, '09-28-2018')
admin_user.privileges.show_privileges()