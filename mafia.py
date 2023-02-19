import random
import os

mafia_names = [
    "Vito Corleone",
    "Michael Corleone",
    "Chief keef",
    "Donnie Brasco",
    "Joey Gallo",
    "Paul Castellano",
    "John Gotti",
    "Lucky Luciano",
    "Meyer Lansky",
    "Sam Giancana",
    "Albert Anastasia",
]

def play_mafia():
    play = input("Would you like to play mafia? (Y/N) ").lower()
    if play != "y":
        print("Maybe next time.")
        return

    player_count = input("Enter the number of players (up to 10): ")
    try:
        player_count = int(player_count)
        if player_count < 1 or player_count > 10:
            raise ValueError
    except ValueError:
        print("Invalid number of players.")
        return

    mafia_names_copy = mafia_names.copy()
    random.shuffle(mafia_names_copy)
    mafia_names_shuffled = [ "Tony Soprano" ] + mafia_names_copy[:player_count - 1]
    random.shuffle(mafia_names_shuffled)
  
    for name in mafia_names_shuffled:
        input("Press enter to see your name.")
        os.system("clear")  # clear screen
        print("Your name is:", name)
        input("Press enter to pass the device to the next player.")
        os.system("clear")  # clear screen

    print("All names have been given.")


play_mafia()
