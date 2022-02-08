import random
import os
from art import logo


def clear_screen():
    os.system("cls" if os.name == 'nt' else 'clear')
    # it's like trinary operator in c/c++.
    # returnsIfTrue if booleanExpression else returnsIfFalse

def deal_card():
    """Returns a random card from the infinite deck of cards"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards"""

    # Check for a blackjack: a hand with only two cards (ace + 10)
    # In case of blackjack, return 0 instead of actual value.
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    # Change value of an ace if it's in the hand and hand is over 21, from 11 to 1.
    if sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack"
    elif user_score == 0:
        return "Win with a Blackjack"
    elif user_score > 21:
        return "You went over. You lose"
    elif computer_score > 21:
        return "Opponent went over. You win"
    elif user_score > computer_score:
        return "You win"
    else:
        return "You lose"
    

def play_game():
    computer_cards = []
    user_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"    Your cards: {user_cards}, current score: {user_score}")
        print(f"    Computer's first card: {computer_cards[0]}")

        # If the computer or the user has a blackjac (i.e. 0) or if the user score is over
        # 21, then end the game.
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    # Once the user is done, it's time for the computer to play. The computer should keep
    # drawing cards as long as it has a score less than 17.
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    # Print final result.
    print(f"    Your final hand: {user_cards}, final score: {user_score}")
    print(f"    Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

print(logo)
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
    clear_screen()
    play_game()

