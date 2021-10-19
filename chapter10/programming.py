# 10-5: Programming Poll
filename = 'chapter10/programming.txt'
polling_active = True

while polling_active:
    # prompt for the person't name and response
    name = input("\nWhat is your name?: ")
    response = input("Why do you like programming?: ")

    with open(filename, 'a') as file_object:
        file_object.write(f"{name}: {response}\n")

    # find out if anyone else is going to take the poll
    repeat = input("\nWould anyone else like to take the poll at this time? (yes/no) ")
    if repeat == 'no':
        polling_active = False
