"""
Comment blocks (like this one): explanations
Grey/Hash comments: typical comments to be expected in any file

This app will ask the user for their name and location and concatenate the two together then print it to the screen.
The comments will explain what each part is doing.

Modules (you can call them anything) are imports from various models (again, call them anything) folders and sub folders.
The dot symbolises a slash therefore models.action_modules is the same as models/action_modules in folder structure.
This is just a Python thing. For instance, JavaScript utilises slash in the familiar way.
You will also see __init__.py files.
These are required (and created by the programmer) to initialise the modules. They just tell Python there's a module located
in that folder, nothing more. The module will NOT import without an __init__.py file present (underscores required).
You can put things in them if you want, this is programmer preference. I personally do not since I prefer my files to be verbose.

Since RootProjectFolder is our root folder in which main.py exists, we do not need to reference it in the from statement but you can
do so if you wish.
"""

# project imports
from models.action_modules.get_location_module import get_location
from models.action_modules.get_username_module import get_username
from models.action_modules.create_sentence_module import create_output_sentence
from models.ui_modules.print_module import print_to_screen

"""
You will notice the modules above are coming from firstly the models folder. This is so all modules are stored in one place.
The folder is further broken down to two subfolders (AKA "nested" folders) called action_modules and ui_modules.
For such a small app you would never do this but for larger projects you absolutely want to know whether you need to
call a UI based module (maybe printing something to screen or rendering something in HTML/markdown) or whether
you need to call a logic-based module such as a calculation of sorts, or in this case a module asking for user input and performing concatenation. 
"""

# ask for user inputs
user_name = get_username()
user_location = get_location()

# create string for output
output_string = create_output_sentence(user_name, user_location)

# print the output to screen
print(output_string)
