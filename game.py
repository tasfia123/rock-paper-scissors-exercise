#game.py
import random
import os 
import dotenv
dotenv.load_dotenv()


PLAYER_NAME = os.getenv("PLAYER_NAME")

print(PLAYER_NAME)
#import dotenv

#dotenv.load_dotenv()

#VAR_NAME = os.getenv("PLAYER_NAME")
#print(VAR_NAME)

print("------------")
print("Welcome", PLAYER_NAME,"to my to my Rock-Paper-Scissors game...")
print("---------------")
#print( 10)
#print ("testing")

#validate the input such that only if it is one of the expected values
#we will continue 
#otherwise we will stop the program before it deos anything else
# and ask the user to run the program again

user_choice = input("Please choose either 'rock', 'paper', or 'scissors': ")
#print("USER CHOICE:")
#print(user_choice)
print("USER CHOICE:", user_choice)

#if user_choice = "rock", "paper", or "scissors"
if  (user_choice == "rock") or ( user_choice == "paper")  or ( user_choice == "scissors"):
    print ("Valid, Keep Going")
else: 
    print ("oops, invalid input. Please try again")
    exit()
   # print("USER CHOICE",user_choice)


valid_options = ["rock", "paper", "scissors"]

computer_choice = random.choice(valid_options)


print("COMPUTER CHOICE:", computer_choice)


# determine who won!

if user_choice == "rock":
    if computer_choice == "rock":
        print("IT'S A TIE, TRY AGAIN")
    elif computer_choice == "paper":
        print("OH, THE COMPUTER WON...")
    elif computer_choice == "scissors":
        print("YOU WON! GOOD JOB!")
elif user_choice == "paper":
    if computer_choice == "rock":
        print("YOU WON! GOOD JOB!")
    elif computer_choice == "paper":
        print("IT'S A TIE, TRY AGAIN")
    elif computer_choice == "scissors":
        print("OH, THE COMPUTER WON...")
elif user_choice == "scissors":
    if computer_choice == "rock":
        print("Oh, the computer won. It's ok")
    elif computer_choice == "paper":
        print("YOU WON! GOOD JOB!")
    elif computer_choice == "scissors":
        print("IT'S A TIE, TRY AGAIN")


print("This is the end of our game, Thanks for playing. Please play again!")




