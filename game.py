#game.py
print("Rock, Paper, Scissors, Shoot!")

#print( 10)
#print ("testing")

#validate the input such that only if it is one of the expected values
#we will continue 
#otherwise we will stop the program before it deos anything else
# and ask the user to run the program again

user_choice = input("Please choose one of 'rock', 'paper', 'scissors': ")
#print("USER CHOICE:")
#print(user_choice)
print("USER CHOICE:", user_choice)

#if user_choice = "rock", "paper", or "scissors"
if  (user_choice == "rock") or ( user_choice == "paper")  or ( user_choice == "scissors"):
    print ("Valid, Keep Going")
else: print ("oops, invalid input. Please try again")
exit()
   # print("USER CHOICE",user_choice)

print("This is the end of our game, please play again")

