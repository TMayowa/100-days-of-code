#using repl.it live IDE
from art import *
import random
from game_data import data
from replit import clear

score = 0
runs = 0

def game():
  '''Runs a higher-lower game'''
  rand_A = random.randint(0,len(data)-1)
  name_A = data[rand_A]["name"]
  follower_count_A = data[rand_A]["follower_count"]
  description_A = data[rand_A]["description"]
  country_A =  data[rand_A]["country"]

  def replay():
    '''Continues the game if the user guesss right'''
    global runs
    global score
    rand_B = random.randint(0,len(data)-1)
    name_B = data[rand_B]["name"]
    follower_count_B = data[rand_B]["follower_count"]
    description_B = data[rand_B]["description"]
    country_B =  data[rand_B]["country"]

    print(logo)
    if score > 0:
      print(f"You're right! current score: {score}")
    print(f"Compare A: {name_A}, {description_A}, {country_A}")
    print(vs)
    print(f"Against B: {name_B}, {description_B}, {country_B}")

    runs += 1
    choice = input("Who has more followers? Type 'A' or 'B': ").lower()
    if choice == "a" and follower_count_A > follower_count_B:
      score += 1
      rand_A = rand_B
      clear()
      game()
    elif choice == "b" and follower_count_B > follower_count_A:
      score += 1
      rand_A = rand_B
      clear()
      game()
    else:
      print(f"Sorry, that's wrong. final score: {score}")
  while score == runs:
    replay()

game()
