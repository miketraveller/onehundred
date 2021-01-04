from replit import clear
from art import logo

print( logo)

bids = {}

bidding = True

while bidding:

    name = input("Enter Name: ")
    bid = input("enter bid: ")

    bids[name] = bid

    keep_going = input("Any more bids? y or n: ")

    if keep_going == 'n':
        bidding = False
    else:
        clear()

ans = max(bids, key=bids.get)

print(f"The winner is {ans}")