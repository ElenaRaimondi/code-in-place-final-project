import json
import random
from fuzzywuzzy import fuzz


DECK_FILE_PATH = "decks/italian_to_english.json"
NUMBER_OF_ROUNDS = 3
NUMBER_OF_ATTEMPTS = 2
POINTS_PER_GUESS = 10
FUZZ_RATIO = 90


score = 0


def intro():
    print("\n\n\n\n* * *\n")
    print("Benvenuto!\n")
    user_name = input("Come ti chiami? ")
    print("\nRules\n")
    return user_name


def load_deck():
    with open(DECK_FILE_PATH, encoding="utf-8") as deck_file:
        deck = json.load(deck_file)
        return deck


def check_correctness(guess, solution):
    correctness = fuzz.ratio(guess, solution)
    return correctness >= FUZZ_RATIO


def practice_card_vocab(card, target_language):
    global score

    for attempt in range(NUMBER_OF_ATTEMPTS):
        guess = input(
            f"How do you say {card['native']} in {target_language}? ")
        solution = card["target"]
        is_correct = check_correctness(guess, solution)
        if is_correct:
            print("Bravo!\n")
            score += POINTS_PER_GUESS
            return
        else:
            print("That's not it!\n")

    print(f"{card['native']} is {solution}. Better luck next time!")


def practice_tense(verb, tense):
    global score

    name, solution = tense
    for attempt in range(NUMBER_OF_ATTEMPTS):
        guess = input(f"What is the {name}? ")

        is_correct = check_correctness(guess, solution)
        if is_correct:
            print("Bravo!\n")
            score += POINTS_PER_GUESS
            return
        else:
            print("That's not it!\n")

    print(f"The {name} of {verb} is {solution}.")


def practice_card_tenses(card, target_language):
    verb = card["verb"]
    print(f"The verb in {target_language} is {verb}. Let's practice the tenses!")
    for tense in card["tenses"]:
        practice_tense(verb, tense)


def practice_deck():
    global score
    score = 0

    deck = load_deck()
    for round in range(NUMBER_OF_ROUNDS):
        print(f"\n* * *\nRound: {round + 1}")
        card = random.choice(deck["cards"])
        deck["cards"].remove(card)
        target_language = deck["language"]["target"]

        if card["type"] == "vocab":
            practice_card_vocab(card, target_language)
        elif card["type"] == "tenses":
            practice_card_tenses(card, target_language)

        print(f"Your score is {score}.")

    print(f"\nYour final score is {score}. Good job!")


def main():
    user_name = intro()
    input(f"Ready, {user_name}? Print enter to start! ")
    practice_deck()
    print("Arrivederci!")


if __name__ == "__main__":
    main()
