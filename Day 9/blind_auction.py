from replit import clear

from art import logo

other_bidder = "yes"
auction = {}

def highest_bidder(auction):
  highest_bid = 0
  winner = ""

  for name in auction:
    bid_amount = auction[name]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = name
  print(f"The winner is {winner} with a bid of {highest_bid}")

while other_bidder == "yes":
  print(logo)
  name = input("what is your name?: ").lower()
  bid = int(input("What is your bid?: $"))
  auction[name] = bid
  
  other_bidder = input("Is anyone still interesting in bidding, yes/no?: ").lower()
  clear()

highest_bidder(auction)


