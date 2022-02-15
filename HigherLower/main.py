import random
from game_data import data
from art import logo
from art import vs
import os

random.shuffle(data)
score = 0

for i in range(len(data) - 1):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(logo)

    if (not i == 0):
        print(f"You're right! Current score: {score}")

    print(f"Compare A: {data[i]['name']}, a {data[i]['description']} from {data[i]['country']}")
    print(f"Follower count: {data[i]['follower_count']}")
    print(vs)
    print(f"Against B: {data[i+1]['name']}, a {data[i]['description']} from {data[i]['country']}")
    
    answer = input("Who has more follower? Type 'A' or 'B': ").lower()
    
    # Check correctness.
    if answer == 'a' and data[i]['follower_count'] > data[i + 1]['follower_count'] or answer == 'b' and data[i]['follower_count'] < data[i + 1]['follower_count']:
        score += 1

    else:
        break

print("Game over!")
print(f"Your score was {score}")