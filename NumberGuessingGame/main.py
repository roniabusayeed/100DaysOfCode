import random

print("Welcome to the Number Guessing Game!")

# Guess a number.
target = random.randint(1, 100)
print("I'm thinking of a number between 1 and 100")

# Ask user their difficulty level.
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
if difficulty == 'easy':
    max_attempts = 10
else:
    max_attempts = 5

won = False
attempts = 0
while attempts < max_attempts:
    print(f"You have {max_attempts - attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))

    if guess == target:
        print("You win!")
        won = True
        break
    elif guess < target:
        print("Too low.")
    else:
        print("Too high.")

    print("Guess again.")
    attempts += 1

if not won:
    print("You lose!")
