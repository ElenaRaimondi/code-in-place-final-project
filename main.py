CARDS_FILE_PATH = "cards/italian_to_english.json"

def intro():
  print("Benvenuto!")
  user_name = input("Come ti chiami? ")
  print("Rules")
  return user_name

def play_new_game():
  score = 0


def main():
  user_name = intro()
  input(f"Ready, {user_name}? Print enter to start! ")
  play_new_game()



if __name__ == "__main__":
    main()