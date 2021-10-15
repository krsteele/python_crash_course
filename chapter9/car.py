# You can modify the attributes of an instance directly or write methods that update attributes in specific ways.

class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        # default attribute
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    # You can have methods that update certain attributes for you.
    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:  
            self.odometer_reading = mileage
        else:
            print("You can't roll back the odometer!")

    # You might want to increment an attribute's value by a certain amount rather than set an entirely new value.
    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles


my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

# One way to modify an attribute's value is to set it directly
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

# Here, we call a method to update the odometer_reading attribute
my_new_car.update_odometer(42)
my_new_car.read_odometer()

# Here, we call a method to increment the mileage by the number passed.
my_new_car.increment_odometer(100)
my_new_car.read_odometer()


# Instances as attributes
# If you find that you have a growing list of attributes and methods and your files are becoming lengthy...
# you might recognize that part of one class can be written as a separate class

# For example, we might notice we're adding many attributes and methods specific to our electric car class's battery. 
# We can move those to their own Battery class
class Battery:
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=75):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size
        
    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315

        print(f"This car can go about {range} miles on a full charge.")

    def upgrade_battery(self):
        if self.battery_size < 100:
            self.battery_size = 100
        else:
            pass



# Inheritance

# When one class inherits from another, it takes on the attributes and methods of the first class.

# parent -- the original class
# child -- the new inheriting class

# The child class can inherit any or all attributes and methods of the parent, but is also free to define
# new attributes and methods of its own.

# When writing a new child class, you'll often want to call the __init__() method from the parent class. 
# This will initialize any attributes that were defined in the parent __init__() method and make them available in the child class.

# Electric Car 
# When you create a child class, the parent class must be part of the current file
# and must appear before the child class in the file. 

# Define the child class
# The name of the parent class must be included in parens in the definition of the child.
class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    # The __init__ method takes in the information required to make a car instance
    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        # super() is a special function that allows you to call a method from the prent class
        # this comes from a convention of calling the parent a superclass and the child a subclass
        super().__init__(make, model, year)
        # Now we can add attributes specific to electric cars
        self.battery = Battery()

    # Now you can add as many attributes and methods as you need to model an electric car 
    # to whatever degree of accuracy you need. 
    # Overriding parent methods -- you can override any method from the parent class that doesn't 
    # fit what you're trying to model with the child class by defining a method
    # in the child class with the same name as the method you want to override. 


my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

new_e_car = ElectricCar('nissan', 'leaf', 2020)
print(new_e_car.get_descriptive_name())
new_e_car.battery.describe_battery()
new_e_car.battery.get_range()
new_e_car.battery.upgrade_battery()
new_e_car.battery.describe_battery()
new_e_car.battery.get_range()