# Import libraries.
import os
import json

# File location of the categories.
file_name = "categories.json"

# Access the file.
if os.path.exists(file_name):
    with open(file_name, "r") as file:
        data = json.load(file)

else:
    data = {}

# Allow users to choose from the options.

# If users choose option 1, allow them to choose and answer a specific quiz.

# If users choose option2, allow them to leave the program.

