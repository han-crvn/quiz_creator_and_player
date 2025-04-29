# Import Libraries.
import os
import json

# File location of the categories.
file_name = "categories.json"

# Allow users to choose from the options.
while True:
    try:
        print("\nSelection:")
        print("1. Add category \n2. Access a category \n3. Exit \n")
        choice = int(input("Enter the number of your choice: "))

        # If users choose option 1, allow them to add category.
        if choice == 1:
            pass
    
        # If users choose option 2, allow them to access category and add question set.
        elif choice == 2:
            pass
    
        # If users choose option 3, allow them to exit the program.
        elif choice == 3:
            break
    
    # Catch invalid input.
    except ValueError:
        print("Invalid input! try again!")