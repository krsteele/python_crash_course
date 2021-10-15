


# 9-1: Restaurant
class Restaurant:
    """An attempt to model a restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant_name and cuisine_type attributes"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Describe the restaurant"""
        print(f"\n{self.restaurant_name} is a restaurant serving {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        """Simulate opening the restaurant"""
        print(f"{self.restaurant_name} is now open!")

    def set_number_served(self, customers):
        """Set number_served to a given value."""
        self.number_served = customers

    def increment_number_served(self, add_customers):
        """Add the given amount to number_served."""
        self.number_served += add_customers


restaurant = Restaurant('La Choza', 'New Mexican')

print("Name: ", restaurant.restaurant_name)
print("Cuisine: ", restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()


# 9-2: Three Restaurants
restaurant_1 = Restaurant('El Fuego', 'Peruvian')
restaurant_2 = Restaurant('Lockeland Table', 'Farm-to-Table')
restaurant_3 = Restaurant('Italia', 'Italian')

restaurant_1.describe_restaurant()
restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()

# 9-4: Number Served
# Add an attribute called number_served with a default value of 0.
restaurant_4 = Restaurant("Newby's Deli", "Deli")
print(restaurant_4.number_served)
# Change the value of number_served and print it again
restaurant_4.number_served = 487
print(restaurant_4.number_served)
# Call the new method set_number_served and set a new value, then print it
restaurant_4.set_number_served(594)
print(restaurant_4.number_served)
# Call the new method increment_number_served and pass it a value to add to the existing value, then print it
restaurant_4.increment_number_served(243)
print(restaurant_4.number_served)


# 9-6: Ice Cream Stand
# Write a class that inherits from the Restaurant class. 
# Add an attribute called flavors that stores a list of ice cream flavors and a method that displays these flavors.

class IceCreamStand(Restaurant):
    """Represent aspects of a restaurant, specific to an ice cream stand."""

    def __init__(self, restaurant_name, cuisine_type):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['vanilla', 'chocolate', 'salty caramel', 'rainbow frozen yogurt', 'pistachio honey', 'strawberry']

    def list_flavors(self):
        """Print a list of available flavors."""
        print(f"\nFlavors available at {self.restaurant_name}")
        for flavor in self.flavors:
            print(f"- {flavor}")


ice_cream = IceCreamStand("Skippy's Ice Creams", "Ice Cream")
print(ice_cream.describe_restaurant())
ice_cream.list_flavors()