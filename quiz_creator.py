# Import Libraries.
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
        print("1. Add category \n2. Access a category \n3. Exit \n")
        choice = int(input("Enter the number of your choice: "))

        # If users choose option 1, allow them to add category.
        if choice == 1:
            while True:
                
                # Allow users to add category and format it to title case.
                category = input("\nEnter the name of the category (0 to go back in main menu): ")
                category = category.title()

                # Check if the category is existing or not.
                if category not in data:
                    data[category] = []
                    print(f"{category} is successfully added!\n")

                    # Add the category to the file.
                    with open(file_name, "w") as file:
                        json.dump(data, file, indent = 4)

                else:
                    print(f"{category} already exists.")

        # If users choose option 2, allow them to access category and add question set.
        elif choice == 2:
            pass
    
        # If users choose option 3, allow them to exit the program.
        elif choice == 3:
            break
    
    # Catch invalid input.
    except ValueError:
        print("Invalid input! try again!")