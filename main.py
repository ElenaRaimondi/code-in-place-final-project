CARDS_FILE_PATH = "cards/italian_to_english.json"

def main():
  user_name, score = intro()
  input(f"Ready, {user_name}? Print enter to start! ")




def intro():
  print("Benvenuto!")
  user_name = input("Come ti chiami? ")
  score = 0
  print("Rules")
  return [user_name, score]


if __name__ == "__main__":
    main()