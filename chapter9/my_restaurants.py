from restaurant import Restaurant, IceCreamStand

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


ice_cream = IceCreamStand("Skippy's Ice Creams", "Ice Cream")
print(ice_cream.describe_restaurant())
ice_cream.list_flavors()