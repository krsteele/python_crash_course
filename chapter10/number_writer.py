# Storing Data
# Using json.dump() and json.load()

# The json.dump() function takes two arguments: 
#   - a piece of data to store and 
#   - a file object it can use to store the data.
import json

numbers = [2,3,5,7,11,13]

filename = 'chapter10/numbers.json'
with open(filename, 'w') as f:
    json.dump(numbers, f)

