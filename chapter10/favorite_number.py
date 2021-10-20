# 10-11: Favorite Number and 10-12: Favorite Number Remembered

import json

def get_stored_number(): 
    """Get stored favorite number if available"""
    filename = 'chapter10/favorite_number.json'
    try:
        with open(filename) as f:
            favorite_number = json.load(f)
    except FileNotFoundError:
        return None
    else: 
        return favorite_number


def get_new_favorite_number():
    """Prompt user for their favorite number."""
    favorite_number = input("What is your favorite number?: ")
    filename = 'chapter10/favorite_number.json'
    with open(filename, 'w') as f:
        json.dump(favorite_number, f)
    return favorite_number
    


def remember_number():
    """Tell user their favorite number."""
    favorite_number = get_stored_number()
    if favorite_number:
        print(f"I know your favoite number! It's {favorite_number}!")
    else:
        favorite_number = get_new_favorite_number()


remember_number()






