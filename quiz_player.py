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

            try: 
                # Allow users to choose from categories.
                selected_choice = int(input("\nEnter the number of the chosen category: "))

                # Access the category.
                category_name = list(data.keys())

                if 1 <= selected_choice <= len(category_name):
                    chosen = category_name[selected_choice - 1]
                    question_set = data[chosen]

                # Add short message.
                print(f"{category_name} is successfully chosen.\n")
                
                # List down the question.
                for number_question, question in enumerate(question_set, 1):
                    print(f"{number}.) {question['question']}\n")

                    # List down the choices.
                    for number_choice, choices in question['choices'].items():
                        print(f"{number_choice}. {choices}")

                    # Allow users to input their answer.
                    chosen_answer = input("\nEnter the letter of correct answer: ")

                    # Access correct answer.
                    correct_answer = question['answer']
                    
                    # Verify if answer is correct.
                    if chosen_answer.upper() == correct_answer.upper():
                        print("Right!")

                    else:
                        print("Wrong!")

            #Catch invalid input.
            except ValueError:
                print("Invalid input! try again.")

        # If users choose option2, allow them to leave the program.
        if choice == 2:
            break
    
    # Catch invalid input.
    except ValueError:
        print("Invalid input! try again.")
