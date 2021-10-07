# Dictionaries
# allow you to connect pieces of related information
# can store almost limitless amount of information

# key-value pairs
alien_0 = {'color': 'green', 'points': 5}
# accessing the value using the key
print(alien_0['color'])
print(alien_0['points'])

new_points = alien_0['points']
print(f"You just earned {new_points} points!")

# Adding new key-value pairs
print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25

print(alien_0)

# starting with an empty dictionary
alien_1 = {}

alien_1['color'] = 'red'
alien_1['points'] = 10

print(alien_1)

# modifying values in a dictionary

print(alien_0)

alien_0['color'] = 'yellow'
print(f"The alien_0 is now {alien_0['color']}.")

# Move the alien to the right.
# Determine how far to move the alien based on its current speed.

alien_0['speed'] = 'medium'
print(f"Original position of alien_0: {alien_0['x_position']}")

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # This must be a fast alien.
    x_increment = 3

# The new position is the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"New position of alien_0: {alien_0['x_position']}")

# Removing key-value pairs
print(alien_0)

del alien_0['points']
print(alien_0)

# A Dictionary of similar objects
# You can also use a dictionary to store one kind of information about many objects. 
favorite_colors = {
    'bobby': 'orange',
    'ashley': 'green',
    'alisha': 'purple',
    'kristen': 'pink',
}

color = favorite_colors['ashley']
print(f"Ashley's favorite color is {color}.")

# Using get() to access values
# To avoid a traceback error if you ask for a value that doesn't exist
# The get() method requires a key as the first argument and you can pass the value to be returned if the key doesn't exist as the second argument

print(alien_1)

x_value = alien_1.get('x_position', 'No x_position assigned')
print(x_value)

# Looping through a dictionary

# Looping through all key-value pairs
user_0 = {
    'username': 'hithere',
    'first_name': 'Cat',
    'last_name': 'Sandwich',
}
# items() returns a list of key-value pairs. 
# The for loop then assigns each of these pairs to the two variables provided. 
for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")

for name, color in favorite_colors.items():
    print(f"\n{name.title()}'s favorite color is {color}.")

# This type of looping would work just as well if our dictionary stored the results from polling a thousand or even a million ppl.

# Looping through all keys in a dictionary
# The keys() method is useful when you don't need to work with all of the values in a dictionary

for name in favorite_colors.keys():
    print(name.title())

# Looping throug the keys is actually the default behavior when looping through a dictionary
# could have just used for name in favorite_colors:
# Use the keys() method explicitly if it makes your code easier to read

# You can access the value associated with any key you care about inside the loop by using the current key

friends = ['bobby', 'ashley']
for name in favorite_colors.keys():
    print(f"hi {name.title()}.")

    if name in friends:
        color = favorite_colors[name]
        print(f"\t{name.title()}, I see you love the color {color}!")

# use the keys() method to find out if a particular key is in the dictionary

if 'erin' not in favorite_colors.keys():
    print("Erin, what is your favorite color?")

# Looping through a dictionary's keys in a particular order
# sometimes you'll want to loop through a dictionary in a different order than the order in which they were inserted

# one way is to sort the keys as they're returned in the for loop
for name in sorted(favorite_colors.keys()):
    print(f"{name.title()}, thank you for taking the color poll.")

# Looping through all values in a dictionary
print("The following colors have been favorited:")
for color in favorite_colors.values():
    print(color)

# You might need to list all values without any repeats
favorite_doughnuts = {
    'jeremy': 'cake',
    'amarilis': 'chocolate-covered',
    'louise': 'glazed',
    'hunter': 'cake',
    'kristen': "jelly-filled",
    'megan': 'chocolate-covered',
    'tim': 'custard-filled',
    'Hilda': 'chocolate-covered',
}

# a set is a collection in which each item must be unique
print("These are our favorite doughnut flavors:")
for flavor in sorted(set(favorite_doughnuts.values())):
    print(flavor)

# You can build a set directly using braces and separating the elements with commas:
languages = {'python', 'ruby', 'python', 'c'}

print(languages)

# unlike lists and dictionaries, sets do not retain items in any specific order

# Nesting

# A List of Dictionaries
invader_0 = {'color': 'green', 'points': 5}
invader_1 = {'color': 'yellow', 'points': 10}
invader_2 = {'color': 'red', 'points': 15}

invaders = [invader_0, invader_1, invader_2]

for invader in invaders: 
    print(invader)

# automatically generate a list of dictionaries

# Make an empty list for storing laser cats
laser_cats = []

# Make 30 laser cats
# range() tells python how many times we want the loop to repeat
for cat_number in range(30):
    new_cat = {'color': 'tuxedo', 'points': 5, 'speed': 'slinking '}
    laser_cats.append(new_cat)

# to change the first three cats use a for loop and if statement
for cat in laser_cats[:3]:
    if cat['color'] == 'tuxedo':
        cat['color'] = 'calico'
        cat['speed'] = 'gamboling'
        cat['points'] = 10

# Show the first 5 laser cats
# here we use a slice to print the first five laser cats
for cat in laser_cats[:5]:
    print(cat)
print("...")

# Show how many laser cats have been created
print(f"Total number of laser cats: {len(laser_cats)}")

# A List in a Dictionary

pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}

print(f"You ordered a {pizza['crust']}-pizza " 
    "with the following toppings:")

for topping in pizza['toppings']:
    print(f"\t{topping}")

# A Dictionary in a Dictionary
# This can get complicated quickly
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton'
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris'
    },
}

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']

    print(f"\tFull name: {full_name.title()}")
    print (f"\tLocation: {location.title()}")


# Exercise 6-1
person_1 = {
    'first': 'bobby',
    'last': 'Gee',
    'age': 40,
    'city': 'Tokyo'
}

print(person_1['first'].title())
print(person_1['last'].title())
print(person_1['age'])
print(person_1['city'].title())

# Exercise 6-2
favorite_numbers = {
    'hunter': 7,
    'conifer': 5,
    'megan': 13,
    'tim': 592,
    'hilda': 6,
}

for friend, number in favorite_numbers.items():
    print(f"{friend.title()}'s favoite number is {number}.")


# Exercise 6-3
glossary = {
    'variables': 'labels that you can assign to values',
    'string': 'a series of characters',
    'float': 'any number with a decimal point',
    'list': 'a collection of items in a particular order',
    'looping': 'running through all entries in a list and performing the same task with each item',
    'dictionary': 'a collection of key-value pairs in python',
}

for word, meaning in glossary.items():
    print(f"\n{word}: {meaning}")


# Exercise 6-4

# Exercise 6-5
rivers = {
    'nile': 'egypt',
    'amazon': 'brazil',
    'mississipi': 'united states',
}

for river, country in rivers.items(): 
    print(f"\nThe {river.title()} river runs through {country.title()}.")


print("Rivers in dictionary:")
for river in rivers.keys():
    print(river.title())


print("Countries with major rivers:")
for country in rivers.values(): 
    print(country.title())


# Exercise 6-6 
poll_prospects = ['bobby', 'ashley', 'alisha', 'kristen', 'tim', 'megan', 'hilda']

for name in favorite_colors.keys():
    if name in poll_prospects:
        color = favorite_colors[name]
        print(f"\n{name.title()}, I see you like the color {color}!")
    else:
        print(f"\n{name.title()}, please take our color poll!")
        # else statement does not work and I don't know why

# Exercise 6-7
person_2 = {
    'first': 'cat',
    'last': 'sandwich',
    'age': 38,
    'city': 'new york'
}
person_3 = {
    'first': 'peter',
    'last': 'piper',
    'age': 100,
    'city': 'peoria'
} 

people = [person_1, person_2, person_3]

for person in people: 
    print(f"\nName: {person['first'].title()} {person['last'].title()}")
    print(f"Age: {person['age']}")
    print(f"City: {person['city'].title()}")