# create a class that represents a dog
class Dog:
    """A simple attempt to model a dog."""

    # A function that's part of a class is called a method. 
    # The __init__ method is a special method that Python runs automatically whenever we create a new instance of an obj based on a class. 
    # The self parameter is required in the method definition for __init__ and must come first before the other parameters. 
    # self is a reference to the instance itself. It gives the individual instance access to the attributes and methods in the class. 
    def __init__(self, name, age):
        """Initialize name and age attributes."""
        # Any variable prefixed with self is available to every method in the class. We'll also be able to access these variavles through any instance created from the class.
        # Variables that are accessible through instances like this are called attributes.
        self.name = name
        self.age = age

    # Since the sit and roll_over methods don't need additional information to run, we just define them to have one parameter, self. 
    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")


# Making an instance from a class
my_dog = Dog('Willie', 6)

# Accessing attributes with dot notation
print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")

# Calling Methods
my_dog.sit()
my_dog.roll_over()

# You can create as many instances from a class as you need.
your_dog = Dog('Lucy', 3)
print(f"Your dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.sit()