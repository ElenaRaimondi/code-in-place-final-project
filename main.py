import json
import random


DECK_FILE_PATH = "decks/italian_to_english.json"
NUMBER_OF_ROUNDS = 3


def intro():
    print("Benvenuto!")
    user_name = input("Come ti chiami? ")
    print("Rules")
    return user_name


def load_deck():
  with open(DECK_FILE_PATH) as deck_file:
    deck = json.load(deck_file)
    return deck


def play_new_game(deck):
    score = 0

    for round in range (NUMBER_OF_ROUNDS):
      card = random.choice(deck["cards"])
      # user plays with that card


def main():
    user_name = intro()
    chosen_deck = load_deck()
    input(f"Ready, {user_name}? Print enter to start! ")
    play_new_game(chosen_deck)


if __name__ == "__main__":
    main()
