# Chapter 7


# 7.1 Rental Car
# car = input("What kind of rental car would you like?: ")

# print(f"\nLet me see if I can find you a {car}.")

# 7.2 Restaurant Seating
# dinner_group = input("How many people are in you dinner group?: ")

# dinner_group = int(dinner_group)

# if dinner_group > 8: 
    # print("You will have a wait for a table.")
# else: 
    # print("Your table is ready.")

# 7.3 Multiples of Ten
# number = input("Pick a number, any number!: ")

# number = int(number)

# if number % 10 == 0: 
    # print(f"\n{number} is a multiple of 10!")
# else: 
    # print(f"\n{number} is not a multiple of 10")

#  Introducing While Loops
# A while loop runs as long as, or while, a certain condition is true. 
# A loop that starts with while True will run forever unless it reaches a break statement. 

# 7-4: Pizza Toppings
# prompt = "\nPlease enter a topping you would like on your pizza. "
# prompt += "\n(If you have entered all your toppings, enter 'quit'.) "

# while True: 
#     topping = input(prompt)

#     if topping == 'quit':
#         break
#     else: 
#         print(f"\nI'll add {topping} to your pizza!")


# 7-5: Movie Tickets
# age = input("\nTell me your age, and I'll tell you the cost of your movie ticket. ")

# age = int(age)

# if age < 3:
#     print(f"\nYour ticket is free.")
# elif age >= 3 and age <= 12:
#     print(f"\nYour ticket is $10.")
# else:
#     print(f"\nYour ticket is $15.")


# 7-6: Three Exits

# Use a conditional test in the while statement to stop the loop
# prompt = "\nPlease enter a topping you would like on your pizza. "
# prompt += "\n(If you have entered all your toppings, enter 'quit'.) "

# count = 0

# while count < 3: 
#     topping = input(prompt)

#     if topping == 'quit':
#         break
#     else: 
#         print(f"\nI'll add {topping} to your pizza!")
#         count += 1


# 7-8: Deli 
# sandwich_orders = ['tuna salad', 'club', 'bahn mi', 'veggie']
# finished_sandwiches = []

# while sandwich_orders:
#     current_sandwich = sandwich_orders.pop()

#     print(f"\nCurrently making your {current_sandwich} sandwich.")
#     finished_sandwiches.append(current_sandwich)

# print(f"\nThe following sandwiches are ready for pickup: ")
# for sandwich in finished_sandwiches:
#     print(f"{sandwich} sandwich")


# 7-9: No Pastrami
from os import name


sandwich_orders = ['tuna salad', 'pastrami','club', 'pastrami', 'bahn mi', 'pastrami', 'veggie']
finished_sandwiches = []

print("The deli is currently out of pastrami. Please place a new order if your order contained pastrami.")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()

    print(f"\nCurrently making your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

print(f"\nThe following sandwiches are ready for pickup: ")
for sandwich in finished_sandwiches:
    print(f"{sandwich} sandwich")


# 7-10: Dream Vacation
# empty dictionary to store poll responses
responses = {}

# flag to indicate polling is active
polling_active = True

while polling_active:
    # prompt for the person't name and response
    name = input("\nWhat is your name? ")
    response = input("Where is your dream vacation spot? ")

    # store the response in the dictionary
    responses[name] = response

    # find out if anyone else is going to take the poll
    repeat = input("\nWould anyone else like to take the poll at this time? (yes/no) ")
    if repeat == 'no':
        polling_active = False

# Polling is complete. Show the results.
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name}'s dream vacation spot is {response}. ")
