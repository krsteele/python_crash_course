# Working with Multiple Files

# def count_words(filename):
#     """Count the approximate number of words in a file."""

#     try:
#         with open(filename, encoding='utf8') as f:
#             contents = f.read()
#     except FileNotFoundError:
#         print(f"Sorry, the file {filename} does not exist.")

#     # analyzing text
#     try:
#         with open(filename, encoding='utf8') as f:
#             contents = f.read()
#     except FileNotFoundError:
#         print(f"Sorry, the file {filename} does not exist.")
#     else:
#         # count the approximate num of words in the file.
#         words = contents.split()
#         num_words = len(words)
#         print(f"The file {filename} has about {num_words} words.")

filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
# for filename in filenames:
#     name = f"chapter10/{filename}"
#     count_words(name)


# 10-10: Common Words

def how_many(file, word):
    try:
        with open(file, encoding='utf8') as f:
            contents = f.read()
    except FileNotFoundError:
        # print(f"Sorry, the file {file} does not exist.")
        pass
    else:
        instances = contents.lower().count(word)
        print(f"The file {file} has about {instances} instances of the word {word}.")


for filename in filenames:
    name = f"chapter10/{filename}"
    how_many(name, 'the ')
