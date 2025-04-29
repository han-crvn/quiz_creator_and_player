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
while True:
    try:
        print("\nSelection:")
        print("1. Play a Quiz \n2. Exit \n")
        
        # Allow users to input their choice.
        choice = int(input("Enter the number of your choice: "))

        # If users choose option 1, allow them to choose and answer a specific quiz.
        if choice == 1:
            
            # Check if there is category in file.
            if not data:
                print("\nThere are currently no categories.\n")
                continue
            
            # List down the categories.
            print("\nCategories: ")
            for number, category in enumerate(data.keys(), 1):
                print(f"{number}. {category}")

        # If users choose option2, allow them to leave the program.
        if choice == 2:
            break
    
    # Catch invalid input.
    except ValueError:
        print("Invalid input! try again.")
