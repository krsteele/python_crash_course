# 10-6: Addition & 10-7: Addition Calculator

print("Give me two numbers, and I'll add them for you.")
print("Enter 'q' to quit.")

done = False

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("\nSecond number: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) + int(second_number)
    except ValueError:
        print("Hmm, it seems those weren't both numbers.")
    else:
        print(answer)
        break
        
