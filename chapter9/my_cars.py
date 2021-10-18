# we can import one or multiple classes from a module
from car import Car, ElectricCar

# or we can import the entire module, but then need to use the module_name.ClassName syntax to access the classes we need.
# import car 

# or we can import all classes from a module. Not recommended. 
# Use one of the other two methods instead to keep your code clear and avoid potential naming conflicts.
# from car import *

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
