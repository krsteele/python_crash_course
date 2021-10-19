# Handling the FileNotFound Exception

filename = 'chapter10/alice.txt'
# The encoding argument is used when your system's default encoding doesn't match the encoding of the file that's being read.
try:
    with open(filename, encoding='utf8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry, the file {filename} does not exist.")

# analyzing text
try:
    with open(filename, encoding='utf8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry, the file {filename} does not exist.")
else:
    # count the approximate num of words in the file.
    words = contents.split()
    num_words = len(words)
    print(f"The file {filename} has about {num_words} words.")
