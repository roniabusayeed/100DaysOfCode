from art import logo
import os

print(logo)

bidding_record = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
    highest_bid = 0  # Assuming all bid amounts will be greater than 0.
    highest_bidder = ""
    for bidder in bidding_record:
        if bidding_record[bidder] > highest_bid:
            highest_bid = bidding_record[bidder]
            highest_bidder = bidder
    return highest_bidder

while not bidding_finished:
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    
    bidding_record[name] = bid
    
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if should_continue == "no":
        bidding_finished = True

    # Clear terminal screen.
    os.system('cls' if os.name == 'nt' else 'clear')

# Find the person (key) with maximum bid (value).
# highest_bidder = max(bid_dictionary, key=bid_dictionary.get)
highest_bidder = find_highest_bidder(bidding_record)

# Display highest bidder with his/her bid amount.
print(f"The winner is {highest_bidder} with a bid of ${max(bidding_record.values())}.")
