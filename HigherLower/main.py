import random
from game_data import data
from art import logo
from art import vs
import os

random.shuffle(data)
score = 0

def format_data(data):
    """Returns a formatted string version of data"""
    return f"{data['name']}, a {data['description']} from {data['country']}"

def check_answer(guess, a_follower_count, b_follower_count):
    """Take the user guess and follower count and return if they got it right"""
    return guess == 'a' and a_follower_count > b_follower_count\
        or guess == 'b' and a_follower_count < b_follower_count

for i in range(len(data) - 1):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(logo)

    if (not i == 0):
        print(f"You're right! Current score: {score}")

    print(f"Compare A: {format_data(data[i])}")
    print(f"Follower count: {data[i]['follower_count']}")
    print(vs)
    print(f"Against B: {format_data(data[i + 1])}")
    
    answer = input("Who has more follower? Type 'A' or 'B': ").lower()
    
    # Check correctness.
    if check_answer(answer, data[i]['follower_count'], data[i+1]['follower_count']):
        score += 1
    else:
        break

print("Game over!")
print(f"Your score was {score}")