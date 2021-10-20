# Writing to an empty file

filename = 'chapter10/programming.txt'
# open has two arguments here
# the name of the file we want to open, and 'w' tells Python that we wantt o open the file in write mode.
# read mode ('r'), write mode ('w'), append mode ('a'), or read and write ('r+'). read-only mode is default if no argument provided.
# the open() function automatically creates the file you're writing to if it doesn't already exist.
# be careful opening a file in write mode. If the file does exist, Python will erase the contents ofthe file before returning the file object.
with open(filename, 'w') as file_object:
    file_object.write("I love programming.")


# ----------------------------
# Python can only write strings to a text file. If you want to store numerical data in a text file,
# you'll have to convert the data to string format first using the str() function
# ----------------------------


# Writing Multiple Lines

# The write() function doesn't add any newlines to the text you write unless you explicitly tell it to.

    file_object.write("\nI love creating new games.")


# Appending to a File
# if you want to add content to a file instead of writing over existing content, 
# you can open the file in append mode. Any lines you write will be added at the 
# end of that file. If the file doesn;t exist yet, Python will create an empty file for you.

with open(filename, 'a') as file_object:
    file_object.write("\nI also love finding meaning in large datasets.")
    file_object.write("\nI love creating apps that can run in a browser.")

