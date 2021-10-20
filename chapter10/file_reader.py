"""program that opens the pi_digits.txt file, reads it, and prints the contents to the screen"""

# the open() function needs one argument, the name of the file you want to open
# the open() function returns an object representing the file
# Python assigns this object to file_object
# the keyword with closes the file once access to it is no longer needed (when the with block finishes execution)
with open('chapter10/pi_digits.txt') as file_object:
    # now that we have a file object representing the file, 
    # we use the read() method to read the entire contents of the file and store it as one long string in contents
    contents = file_object.read()
# when we print the value of contents, we get the entire text file back
print(contents)


# Reading Line by Line
filename = 'chapter10/pi_digits.txt'

with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())


# Making a List of Lines from a File

# when you use with, the file object returned by open() is only available inside with with block that contains it.
# if you want to retain access to a file's contents outside the with block
# you can store the file's lines inside a list inside the block and then work with that list.
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