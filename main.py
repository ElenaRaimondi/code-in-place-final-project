import json
import random


DECK_FILE_PATH = "decks/italian_to_english.json"
NUMBER_OF_ROUNDS = 3
NUMBER_OF_ATTEMPTS = 2


def intro():
    print("Benvenuto!")
    user_name = input("Come ti chiami? ")
    print("Rules")
    return user_name


def load_deck():
    with open(DECK_FILE_PATH, encoding="utf-8") as deck_file:
        deck = json.load(deck_file)
        return deck


def practice_card_vocab(card):
    for attempt in range(NUMBER_OF_ATTEMPTS):
        guess = input(
            f"How do you say {card['native']} in your target language? ")
        if guess == card["target"]:
            print("Bravo!")
            return
        else:
            print("That's not it!")

    print(f"{card['native']} is {card['target']}. Better luck next time!")


def practice_tense(verb, tense):
    # name = tense[0]
    # solution = tense[1]
    name, solution = tense
    for attempt in range (NUMBER_OF_ATTEMPTS):
        guess = input(f"What is the {name}? ")

        if guess == solution:
            print("Bravo!")
            return
        else:
            print("That's not it!")

    print(f"The {name} of {verb} is {solution}.")


def practice_card_tenses(card):
    verb = card["verb"]
    print(f"The verb is {verb}")
    for tense in card["tenses"]:
        practice_tense(verb, tense)


def practice_deck(deck):
    score = 0

    for round in range(NUMBER_OF_ROUNDS):
        print(f"Round: {round + 1}")
        card = random.choice(deck["cards"])

        if card["type"] == "vocab":
            practice_card_vocab(card)
        elif card["type"] == "tenses":
            practice_card_tenses(card)

        print(f"Your final score is {score}. Good job!")


def main():
    user_name = intro()
    chosen_deck = load_deck()
    input(f"Ready, {user_name}? Print enter to start! ")
    practice_deck(chosen_deck)
    print("Arrivederci!")


if __name__ == "__main__":
    main()
