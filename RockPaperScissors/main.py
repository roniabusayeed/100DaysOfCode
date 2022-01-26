rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

choice = int(input("What do you choose? Type 0 for Rock, 1 for Papers, 2 for Scissors\n"))

if choice == 0:
    print(rock)
elif choice == 1:
    print(paper)
elif choice == 2:
    print(scissors)

computer_choice = random.randint(0, 2)

print("Computer chose:")
if computer_choice == 0:
    print(rock)
elif computer_choice == 1:
    print(paper)
elif computer_choice == 2:
    print(scissors)

# Determine winner.
player_wins = False
draw = False
if choice == 0:
    # Player chose Rock. Now he can only win if the 
    # computer chooses Scissors.
    if computer_choice == 2:
        player_wins = True
    elif computer_choice == 0:
        draw = True

elif choice == 1:
    if computer_choice == 1:
        draw = True
    elif computer_choice == 0:
        player_wins = True
elif choice == 2:
    if computer_choice == 1:
        player_wins = True
    elif computer_choice == 2:
        draw = True

# Display output.
if draw:
    print("It's a draw")
elif player_wins:
    print("You win!")
else:
    print("Computer wins!")
