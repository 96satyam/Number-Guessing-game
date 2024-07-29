#Number Guessing Game Objectives:



# Include an ASCII art logo.
logo = """|  __ \                     |_   _| |          | \ | |               | |              
| |  \/_   _  ___  ___ ___    | | | |__   ___  |  \| |_   _ _ __ ___ | |__   ___ _ __ 
| | __| | | |/ _ \/ __/ __|   | | | '_ \ / _ \ | . ` | | | | '_ ` _ \| '_ \ / _ \ '__|
| |_\ \ |_| |  __/\__ \__ \   | | | | | |  __/ | |\  | |_| | | | | | | |_) |  __/ |   """

import random
print("Welcome to the Number Guessing Game!\n")
print("I'm thinking of a number between 1 and 100.\n")
number = random.randint(1,100)
print(f"Correct number is {number}")
choice = input("Choose a difficulty. Type 'easy' or 'hard': ")
if choice  == 'easy':
  attempts = 10
else:
  attempts = 5

print(f"You have {attempts} attempts remaining to guess the number.")
Guess = int(input("Make a guess:  "))
while attempts > 0:
  
  if Guess > number:
    print("Too high.")
    attempts-=1
    if attempts==0:
      print("You are out of attempts. You lose.")
      break
    else:
      print("Guess again.")
    print(f"You have {attempts} attempts remaining to guess the number.")
    Guess = int(input("Make a guess:  "))
  elif Guess < number :
    print("Too low.")
    attempts-=1
    if attempts==0:
      print("You are out of attempts. You lose.")
      break
    else:
      print("Guess again.")
    print(f"You have {attempts} attempts remaining to guess the number.")
    Guess = int(input("Make a guess:  "))

  else:
    print(f"You got it! The answer was {number}.")
    break
   
  

  

# Allow the player to submit a guess for a number between 1 and 100.

# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

