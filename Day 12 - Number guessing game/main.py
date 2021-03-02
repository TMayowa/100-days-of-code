# using the live IDE repl.it

import random
from replit import clear
from art import logo

def game():
  print(logo)
  print("Welcome to the gessing game!")
  print("I am thinking of a number between 1 and 100")

  lives = 0 
  difficulty = input("choose a difficulty. Type 'easy' or 'hard': ").lower()
  if difficulty == "easy":
    lives = 10
  elif difficulty == "hard":
    lives = 5

  random_num = random.randint(1,100)

  while lives > 0:
    print(f"You have {lives} attempts remaining to guess the number")
    guess = int(input("Make a guess: "))
    if guess > random_num:
      print("Too high")
      lives -= 1
      if lives != 0:
        print("Guess again")
    elif guess < random_num:
      print("Too_low")
      lives -= 1
      if lives != 0:
        print("Guess again")
    elif guess == random_num:
      print("You got it, the answer was 12")
      lives = -1
  if lives == 0:
    print(f"you lost, the number is {random_num}")

game()
replay = input("Do you want to play again? y/n: ").lower()
if replay == "y":
  clear()
  game()
