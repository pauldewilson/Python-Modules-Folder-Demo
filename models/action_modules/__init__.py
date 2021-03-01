def get_username():
    """
    Asks input from user and returns it as a variable
    """
    username = input("Input username: ")
    return username

def get_location():
    """
    Asks input from user and returns it as a variable
    """
    location = input("Input location: ")
    return location

def create_output_sentence(name, loc):
    return f"The user is called {name} and their location is {loc}"

def print_to_screen(inp):
    """
    Takes an input and prints to screen
    """
    print(inp)
