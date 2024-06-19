import random

winCases = {
    "snake":"water",
    "water":"gun",
    "gun": "snake"
}

print("Welcome to Snake-Water-Gun Game")
print('''
Mode1 : Duo
Mode2 : Computer
''')
mode = input("What mode you want to play ? :  ")


#Code For Computer
if(mode.lower() == "computer") :
    computer_choice = (random.choice(list(winCases)))
    user_name = input("Enter your name: ")
    user_choice = input("Enter your choice: ")

    if(user_choice == computer_choice):
        print("Tie!!")
    elif(winCases[user_choice.lower()] == computer_choice):
        print(f"{user_name.title()} win!")
    else:
        print(f"{user_name.title()} lose!")
# Code For  Duo
elif(mode.lower() == "duo") :
    user1_name = input("Enter your name: ")
    user2_name = input("Enter your name: ")

    user1_choice = input("Enter your choice: ")
    user2_choice = input("Enter your choice: ")

    if(user1_choice == user2_choice):
        print("Tie!!")
    elif(winCases[user1_choice.lower()] == user2_choice.lower()):
        print(f"{user1_name.title()} win the game!")
    else:
        print(f"{user2_name.title()} win the game!")
else:
    print("Invalid input")
    print("Please try again")