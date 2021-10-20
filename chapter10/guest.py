# 10-3: guest
filename = 'chapter10/guest.txt'

guest_name = input("Welcome! What is your name?: ")
with open(filename, 'w') as file_object:
    file_object.write(f"{guest_name}\n")

# 10-4: guest book
filename_2 = 'chapter10/guest_book.txt'

guest_book_open = True

while guest_book_open: 
    guest_name = input("\nWelcome! What is your name?: ")
    print(f"\nHello, {guest_name}!")

    with open(filename_2, 'a') as file_object:
        file_object.write(f"{guest_name}\n")

    repeat = input("\nWould anyone else like to sign in? yes/no: ")

    if repeat == 'no':
        guest_book_open = False