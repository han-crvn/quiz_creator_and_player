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

# Add short opening message.
print("Hello! This is Quizzo.")

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

                # Allow users to suddenly break from the option.
                if category == 0:
                    break

                # Check if the category is existing or not.
                if category not in data:
                    data[category] = []
                    print(f"{category} is successfully added!\n")

                    # Add the category to the file.
                    with open(file_name, "w") as file:
                        json.dump(data, file, indent = 4)

                else:
                    print(f"{category} already exists.\n")

                break

        # If users choose option 2, allow them to access category and add question set.
        elif choice == 2:
            
             # Check if there is category in file.
            if not data:
                print("\nThere are currently no categories.\n")
                continue
            
            # List down the categories.
            print("\nCategories: ")
            for number, category in enumerate(data.keys(), 1):
                print(f"{number}. {category}")

            try:

                # Allow users to choose from categories.
                selected_choice = int(input("\nEnter the number of the chosen category (0 to go back in main menu): "))

                 # Allow users to suddenly break from the option.
                if selected_choice == 0:
                    continue
                
                # Access the category.
                if selected_choice < 1 or selected_choice > len(data):
                    print("Invalid category number! Returning to menu.")
                    continue
                
                category_name = list(data.keys())[selected_choice - 1]
                
                # Short message.
                print(f"{category_name} is successfully chosen.\n")

                while True:
                    
                    # Enter the question.
                    question = input("Enter the question: ").strip()
                    
                    # Catch empty choices.
                    if not question:
                        print("\nQuestion cannot be empty. Try again.\n")
                        continue

                    # Add the choices to dictionary.
                    choices = {}

                    # Loop the A, B, C, and D choices.
                    for number in range(4):
                        option = chr(65 + number)
                        while True:
                            
                            # Allow users to input choices.
                            choice_input = input(f"Enter choice '{option}': ").strip()
                            
                            # Chech the input.
                            if choice_input:
                                choices[option] = choice_input
                                break
                            
                            # Catch empty choices.
                            else:
                                print("\nChoice cannot be empty. Try again.")

                    # Enter the correct answer.
                    while True:
                        answer = input("Enter the correct answer (A, B, C, D): ").upper()
                        if answer in choices:
                            break
                        
                        # Catch invalid answer.
                        else:
                            print("Invalid answer! Try again.\n")

                    # Add question set
                    data[category_name].append({
                        "question": question,
                        "choices": choices,
                        "answer": answer
                    })

                    with open(file_name, "w") as file:
                        json.dump(data, file, indent=4)

                    # Short message.
                    print("The question set is successfully added.\n")

                    while True:
                        
                        # Ask users if they want to add more question.
                        try_again = input("\nDo you want to enter another question set (1 = Yes, 2 = No): ")
                        
                        # continue outer while loop to add another question.
                        if try_again == "1":
                            break
                        
                        # exit both inner loops
                        elif try_again == "2":
                            raise StopIteration
                        
                        # Catch invalid input.
                        else:
                            print("\nInvalid input! Try again.\n")
            
            # Catch invalid input.
            except ValueError:
                print("Invalid input! Try again.\n")
            
            # Catch the looping.
            except StopIteration:
                pass

        # If users choose option 3, allow them to exit the program.
        elif choice == 3:
            print("Goodbye! Thank you for using Quizzo.")
            break
        
        # Catch invalid input.
        else:
            print("Invalid input! try again!")

    # Catch invalid input.
    except ValueError:
        print("Invalid input! try again!")