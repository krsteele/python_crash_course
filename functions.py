# Chapter 8 exercises

# 8-1: Message

def display_message():
    """ prints a statement about what I'm learning in chapter 8 """
    print("Chapter 8 is all about Python functions!")


display_message()


# 8-2: Favorite Book 

def favorite_book(title):
    """ takes one argument and prints a statement about it """
    print(f"\nOne of my favorite books is {title}.")


favorite_book("Animal, Vegetable, Miracle")


# Passing Arguments

# Positional Arguments need to be in the same order the parameters were written.
# Keyword Arguments - each argument consists of a variable name and a value
# Lists and Dictionaries - can also use lists and dictionaries of values


# 8-3: T-shirt

def make_shirt(size, message_text):
    """Display information about t-shirts being made"""
    print(f"\nYou ordered a {size} shirt that says '{message_text}'.")


make_shirt("large", "Boy, Man, God, Shit")
make_shirt(message_text="Girl, Woman, Goddess, Shit", size="small")


# 8-4: Large Shirts

def make_shirt(size='large', message_text='I love Python'):
    """Display information about t-shirts being made"""
    print(f"\nYou ordered a {size} shirt that says '{message_text}'.")


make_shirt()
make_shirt(size="medium")
make_shirt("small", "But first, coffee.")


# 8-5: Cities 

def describe_city(city, country='Canada'):
    "Display information describing a city"
    print(f"\n{city.title()} is in {country.title()}.")


describe_city("paris")
describe_city("London", "England")
describe_city("Quebec")


# 8-6: City Names

def city_country(city, country):
    "Returns a formatted city and country"
    formatted = f"{city}, {country}"
    return formatted


pair1 = city_country("Paris", "France")
pair2 = city_country("London", "England")
pair3 = city_country("Milan", "Italy")

print(pair1)
print(pair2)
print(pair3)


# 8-7: Album

def make_album(artist_name, album_title, num_songs=None):
    """Return a dictionary containing information about a new album"""
    new_album = {'artist_name': artist_name, 'album_title': album_title}
    if num_songs:
        new_album['num_songs'] = num_songs
    return new_album


album_1 = make_album("Cat Sandwich", "Meow Mix Remix")
album_2 = make_album("Lead Foot", "The Problem with You", 26)
album_3 = make_album("Smithy Jones and the Lo Riders", "If I was")

print(album_1)
print(album_2)
print(album_3)


# 8-8: User Albums

# while True:
#     print("\nI'm going to ask you some questions.")
#     print("Enter 'q' at any time to quit this program.")

#     artist = input("\nWhat is the name of your favorite musical artist?: ")
#     if artist == 'q':
#         break

#     album = input("\nWhat is your favorite album of theirs?: ")
#     if album == 'q':
#         break

#     favorite_album = make_album(artist, album)
#     print(favorite_album)


# 8-9: Messages

print("\nThis function will print a list of text messages.\n")

def show_messages(messages):
    for message in messages:
        print(message)


texts = ["Hey", "What you doin tonight?", "Wanna get some pizza?"]

show_messages(texts)


# 8-10: Sending Messages 

print("\nThis function will print a list of text messages and move the printed ones to a new list.\n")

def send_messages(unsent, sent):
    """
    Simulate sending text messages from a list, until none are left.
    Move each text to a completed list after sending.
    """
    while unsent:
        sending = unsent.pop()
        print(f"\n{sending}")
        sent.append(sending)

unsent_messages = ["can you pick up some milk on your way?", "sure. anything else?", "maybe a bottle of something for mama?", "you got it"]
sent_messages = []

send_messages(unsent_messages, sent_messages)
print("\nlist of unsent: ", unsent_messages)
print("\nlist of sent: ", sent_messages)


# 8-11: Archived Messages

print("\nThis function is the same as above, but maintains the integrity of the original list.\n")

def send_messages(unsent, sent):
    """
    Simulate sending text messages from a list, until none are left.
    Move each text to a completed list after sending.
    """
    while unsent:
        sending = unsent.pop()
        print(f"\n{sending}")
        sent.append(sending)

unsent_messages = ["can you pick up some milk on your way?", "sure. anything else?", "maybe a bottle of something for mama?", "you got it"]
sent_messages = []

send_messages(unsent_messages[:], sent_messages)
print("\nlist of unsent: ", unsent_messages)
print("\nlist of sent: ", sent_messages)


# 8-12: Sandwiches

print("\nHere, we will practice using arbitrary arguments, *args.\n")

def make_sandwich(*items):
    """Summarize the sandwich we are about to make."""
    print("\nMaking a sandwich with the following items: ")
    for item in items:
        print(f"- {item}")


make_sandwich("tuna salad", "cheese", "mayo")
make_sandwich("cheese")
make_sandwich("ham", "cheese", "turkey", "bacon", "mayo", "mustard")


# 8-13: User Profile

print("\nHere, we will practice using arbitrary keyword arguments, **kwargs.\n")

def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


user_profile = build_profile('kristen', 'steele', occupation='software developer', location='nashville, tn', eye_color='green', hair_color='purple')
print(user_profile)


# 8-14: Cars 

print("\nMore practice using arbitrary keyword arguments, **kwargs.\n")

def make_car(make, model, **car_info):
    """Build a dictionary containing info about a car"""
    car_info['make'] = make
    car_info['model'] = model
    return car_info


car = make_car('subaru', 'outback', color='blue', roof_rack=True)
print(car)


# 8-15: Printing Models
# see printing_functions.py and printing_models.py



