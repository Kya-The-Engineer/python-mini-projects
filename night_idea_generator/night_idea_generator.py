"""
Night Idea Generator
____________________
A simple Python program that suggests ideas for:
- Friends Night
- Girls Night
- Date Night

Run this file, choose a vibe, and get a random idea.
"""

import random

def get_night_type():
    """Ask the user what kind of night they want."""
    print("Night Idea Generator")
    print("What kind of night are you planning?")
    print("1 - Friends Night")
    print("2 - Girls Night")
    print("3 - Date Night")
    print("4- Surprise me")

    choice = input("Enter 1, 2, 3,or 4: ")

    options = {
         "1": "friends",
         "2": "girls",
         "3": "date",
         "4": "random",
    }

    return options.get(choice, "random")

def get_idea(night_type):
    """Return a random idea based on the night type."""
    ideas = {
       "friends": [
           "Game night with snacks and card games.",
           "Movie marathon with a fun theme (90s, horror, rom-com).",
           "Potluck dinner where everyone brings a dish.",
           "DIY taco bar with music and dancing in the living room.",
       ],
          "girls": [
               "At home spa night with face masks and candles.",
               "Vision board and manifestation with music.",
               "Sip & paint night with mocktails or wine.",
               "Pajamas, popcorn, and a nostalgic TV show binge.",
       ],
         "date": [
            "Cook a new recipe together and have a candlelit dinner.",
            "Picnic in the living room with a playlist and board game.",
            "Stargazing with deep conversation prompts.",
            "Make dessert together and have a movie or music night.",
       ],
    }

    if night_type == "random":
         all_ideas = ideas["friends"] + ["girls"] + ["date"]
         return random.choice(all_ideas)
    return random.choice(ideas[night_type])


def main():
    night_type = get_night_type()
    idea = get_idea(night_type)

    print("\nHere's an idea for your night:")
    print(f" {idea}")
    print("\nHave fun!")

if __name__ == "__main__":
    main()
      
      

  

