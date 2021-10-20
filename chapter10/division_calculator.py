# Whenever an error occurs that makes Python unsure what to do next, it creates an exception object.
# If you write code that handles the exception, the program will continue running. 
# If you don't handle the exception, the program will halt and show a traceback, which includes a report of the exception that was raised.
# Exceptions are handled in try-except blocks. 
# A try-except block asks Python to do somethign, but it also tells Python what to do if an exception is raised.
# When you use try-except blocks, your programs will continue running even if things start to go wrong.
# Instead of tracebacks, users will see friendly error messages.

# Handling the ZeroDivisionError Exception

# Usng try-except blocks
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")


# Using exceptions to prevent crashes
# the else block

# Any code that depends on the try block executing successfully goes in the else block.

print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("\nSecond number: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by zero!")
    else:
        print(answer)

    