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

                break

        # If users choose option 2, allow them to access category and add question set.
        elif choice == 2:
            
            # Check if there is category in file.
            if not data:
                print("\nThere are currently no categories.\n")
                continue
            
            # List down the categories
            print("\nCategories: ")
            for number, category in enumerate(data.keys(), 1):
                print(f"{number}. {category}")

            try: 
                # Allow users to choose from categories.
                selected_choice = int(input("\nEnter the number of the chosen category: "))

                # Access the category
                category_name = list(data.keys())[selected_choice -1]
                
                # Add short message.
                print(f"{category_name} is successfully chosen.\n")

                while True:

                    # Enter the question.
                    question = input("Enter the question: ")

                    # Enter the choices.
                    choices = {}
                    for number in range(4):
                        option = chr(65 + number)
                        choices[option] = input(f"Enter choice '{option}': ")
                    
                    # Enter the correct answer.
                    while True:
                        answer = input("Enter the correct answer: ").upper()

                        # Check if the answer is in the choices.
                        if answer in choices:
                            break

                        else:
                           print("Invalid answer! try again.")
                    
                    # Add the question set to the chosen category.
                    data[category_name].append({
                        "question": question,
                        "choices": choices,
                        "answer": answer
                    })

                    with open(file_name, "w") as file:
                        json.dump(data, file, indent = 4)

                    # Add short message.
                    print("The question set is successfully added.\n")

                    while True:
                        try:
                            # Ask users if they want to add more question set.
                            try_again = int(input("Do you want to enter another question set (1 = Yes, 2 = No): "))

                            if try_again == 1:
                                continue

                            elif try_again == 2:
                                break
                            
                            else:
                                print("Invalid input! try again.\n")

                        # Catch invalid input.
                        except ValueError:
                            print("Invalid input! try again.\n")

                    break

            # Catch invalid input.
            except ValueError:
                print("Invalid input! try again.\n")

        # If users choose option 3, allow them to exit the program.
        elif choice == 3:
            print("Goodbye! Thank you for using Quizzo.")
            break
    
    # Catch invalid input.
    except ValueError:
        print("Invalid input! try again!")