import json

filename = 'chapter10/username.json'

with open(filename) as f:
    username = json.load(f)
    print(f"Welcome back, {username}!")