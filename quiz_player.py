# Import libraries.
import os
import json
import random

# File location of the categories.
file_name = "categories.json"

# Access the file.
if os.path.exists(file_name):
    with open(file_name, "r") as file:
        data = json.load(file)

else:
    data = {}

# File location of the data information.
data_information = "data_information.json"

# Access the file.
if os.path.exists(data_information):
    with open(data_information, "r") as file:
        data_infos = json.load(file)

else:
    data_infos = {}

# Add variables for score.
score = 0

# Allow users to choose from the options.
while True:
    try:
        print("\nSelection:")
        print("1. Play a Quiz \n2. View History \n3. Exit \n")
        
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
                print(f"{chosen} is successfully chosen.\n")
                
                # Ask for the name of the users.
                users_name = input("Enter your name: ")

                # Initialize user data if not present
                if users_name not in data_infos:
                    data_infos[users_name] = []

                # Randomize the questions.
                random.shuffle(question_set)

                # Limits the number of questions to be ask.
                amount_questions = 5
                selected_questions = question_set[:min(amount_questions, len(question_set))]

                # List down the question.
                for number_question, question in enumerate(selected_questions, 0):
                    print(f"{number_question + 1}.) {question['question']}\n")

                    # List down the choices.
                    for number_choice, choices in question['choices'].items():
                        print(f"{number_choice}. {choices}")

                    # Allow users to input their answer.
                    chosen_answer = input("\nEnter the letter of correct answer: ")

                    # Access correct answer.
                    correct_answer = question['answer']
                    
                    # Verify if answer is correct.
                    if chosen_answer.upper() == correct_answer.upper():
                        print("Right!\n")
                        score += 1

                    else:
                        print("Wrong!\n")
                
                # Show the score of the users.
                if score == 5:
                    print(f"Congratulations {users_name.title()}! You got {score}/{amount_questions}.")

                elif 2 < score <= 4:
                    print(f"Nice Job {users_name.title()}! You got {score}/{amount_questions}.")

                elif score <= 2:
                    print(f"Better Luck Next Time {users_name.title()}! You got {score}/{amount_questions}.")

                data_infos[users_name].append({
                    "Category": chosen,
                    "Score": score,
                })

                with open(data_information, "w") as file:
                    json.dump(data_infos, file, indent = 4)

            #Catch invalid input.
            except ValueError:
                print("Invalid input! try again.\n")

        # If users choose option 2, allow them to access the history of users.
        elif choice == 2:
            
            # Check if there is names in file.
            if not data_infos:
                print("\nThere are currently no entry.\n")
                continue
            
            # List down the names.
            print("\nUsers' History: ")
            for number, name in enumerate(data_infos.keys(), 1):
                print(f"{number}. {name}")

            try: 
                # Allow users to choose from names.
                selected_name = int(input("\nEnter the number of the chosen users' name: "))

                # Access the name.
                access_users = list(data_infos.keys())

                if 1 <= selected_name <= len(access_users):
                    chosen_name = access_users[selected_name - 1]
                    users_data = data_infos[chosen_name]

                    # Check the history of the users and print it.
                    if users_data:
                        print(f"\n{name}'s history: ")

                        # List down their history.
                        for number_entry, entry in enumerate(users_data, 1):
                            print(f"{number_entry}. Category: {entry['Category']} - Score: {entry['Score']}/5")
                
                # Catch invalid input.
                else:
                    print("Invalid selection. Please enter a valid number.")
            # Catch invalid input.
            except ValueError:
                print("Invalid input! try again.\n")

        # If users choose option 3, allow them to leave the program.
        elif choice == 3:
            break

    # Catch invalid input.
    except ValueError:
        print("Invalid input! try again.\n")
