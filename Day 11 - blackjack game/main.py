############### Blackjack Project #####################

#Using repl.it live IDE

from art import logo
from replit import clear
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
  ''' a function that deals random cards to players'''
  return random.choice(cards)

def calculate_score(list):
  ''' a function used to calculate the player scores'''
  if 11 in list and sum(list) > 21:
    list.remove(11)
    list.append(1)
      
  if list[0]+list[1] == 21:
    return 0
  else:
    return sum(list)

def compare(scoreA,scoreB):
  '''a function used to compare user scores. first input is for the player, second input is for the computer'''
  if scoreA == scoreB:
    print("It's a tie")
  elif scoreA == 0 or scoreA == 21 or scoreB > 21 :
    print("You win")
  elif scoreB == 0 or scoreB == 21 or scoreA > 21:
    print("You lose")
  elif scoreA > scoreB:
    print("You win")
  else:
    print("you lose")

restart = "y"

while restart == "y":
  print(logo)
  user_cards = []
  computer_cards = []

  for i in range(0,2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
  
  print(f"Your cards are {user_cards}")
  print(f"the computers first card is {computer_cards[0]}")



  def game():
    '''a function for a new deal'''
    replay = input("Do you want to play another card? y/n: ")
    if replay == "y":
      user_cards.append(deal_card())
      print(f"Your cards are {user_cards}")
      game()
    elif replay == "n":
      while sum(computer_cards) <= 17:
        computer_cards.append(deal_card())

  game()

  print(f"The computers cards are {computer_cards}")

  user_score = calculate_score(user_cards)
  computer_score = calculate_score(computer_cards)

  compare(user_score,computer_score) 
  
  restart = input("Do you want to restart the game?y/n: ")
  if restart == "y":
    clear()
      




