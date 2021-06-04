first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"

print(full_name)
message = f"Hello, {full_name.title()}!"
print(message)

# To add a tab to your text use \t
print("\tPython")

# To add a new line in a string use \n
print("Languages:\nPython\nC\nJavascript")

# Combine the two
print("Languages:\n\tPython\n\tC\n\tJavascript")

# Strip whitespace
favorite_language = 'python '
# .rstrip() strips white space from the right of a string temporarily
favorite_language.rstrip()
# To remove the whitespace permanently
favorite_language = favorite_language.rstrip()

favorite_language = ' python'
# left strip whitespace
favorite_language.lstrip()

favorite_language = ' python '
# strip whitespace from both sides
favorite_language.strip()

# These methods are most often used to clean up user input before it's stored in a program

