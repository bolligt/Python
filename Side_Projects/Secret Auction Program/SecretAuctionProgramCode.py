# Program will ask the first person to enter their name and their bid
# Store this in a dictionary
# Ask if there are other bidders and continue if Yes, end if No
# After all bids are entered determine the highest bidder and their bid

from IPython.display import clear_output
from art import logo

print(logo)
print("Welcome to the secret auction program.")

bids = {}
auction_on = True

while auction_on:
    bidder = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))

    bids[bidder] = bid

    keep_bidding = input("Are there any other bidders? Type 'yes' or 'no'.").lower()
    
    if keep_bidding == 'no':
        clear_output()
        auction_on = False
    else:
        clear_output()

top_bidder = max(bids, key=bids.get)

print(f"The winner is {top_bidder} with a bid of ${bids[top_bidder]}.")