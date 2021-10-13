# 9-1 and 9-2

# 9-1: Restaurant
class Restaurant:
    """An attempt to model a restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant_name and cuisine_type attributes"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Describe the restaurant"""
        print(f"\n{self.restaurant_name} is a restaurant serving {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        """Simulate opening the restaurant"""
        print(f"{self.restaurant_name} is now open!")


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