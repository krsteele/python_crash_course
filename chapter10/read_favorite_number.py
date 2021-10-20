# 10-11: Favoite number
import json

filename = 'chapter10/favorite_number.json'

with open(filename) as f:
    favorite_number = json.load(f)
    print(f"I know your favoite number! It's {favorite_number}!")
