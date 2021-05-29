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


def practice_card_vocab(card):
  pass


def practice_card_tenses(card):
  pass


def practice_deck(deck):
    score = 0

    for round in range (NUMBER_OF_ROUNDS):
      card = random.choice(deck["cards"])
      if card["type"] == "vocab":
        practice_card_vocab(card)
      elif card["type"] == "tenses":
        practice_card_tenses(card)


def main():
    user_name = intro()
    chosen_deck = load_deck()
    input(f"Ready, {user_name}? Print enter to start! ")
    practice_deck(chosen_deck)


if __name__ == "__main__":
    main()
