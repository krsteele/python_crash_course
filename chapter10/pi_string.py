filename = 'chapter10/pi_digits.txt'

with open(filename) as file_object:
    # takes each line from the file and stores it in a list, which we can continue to work with after the with block ends.
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())


# Working iwth a File's Contents

# build a single string containing all the digits in the file with no whitespace
pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))


# Large Files: One Million Digits
filename_2 = 'chapter10/pi_million_digits.txt'

with open(filename_2) as file_object:
    million = file_object.readlines()

pi_mil_str = ''
for mil in million:
    pi_mil_str += mil.strip()

print(f"{pi_mil_str[:52]}...")
print(len(pi_mil_str))


# Is Your Birthday Contained in Pi?
birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_mil_str:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")
    