import json

def get_stored_username():
    """Get stored username if available."""
    filename = 'chapter10/username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """Prompt for a new username."""
    username = input("What is your name? ")
    filename = 'chapter10/username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    print(f"We'll remember you when you come back, {username}!")
    return username


def verify_user(name):
    verify = input(f"Is {name} your name? (yes/no): ")
    if verify == 'yes':
        return verify
    else: 
        get_new_username()
    

def greet_user():
    """Greet the user by name."""
    username = get_stored_username()
    if username:
        verified = verify_user(username)
        if verified:
            print(f"Welcome back, {username}!")    
    else:
        username = get_new_username()
        

greet_user()