import random
def generate_affirmation(category, affirmations_dict):
    return random.choice(affirmations_dict[category])
def main():
    affirmations = {
        "Confidence": [
            "I trust myself and my decisions.",
            "I am capable of handling whatever comes my way.",
            "I show up as my full authentic self"
        ],
        "Calm": [
            "I am safe, grounded, and at peace.",
            "I release what I cannot control.",
            "My breath brings me back to calm"
        ],
        "Focus": [
            "I take things one step at a time.",
            "Progress matters more than perfection.",
            "I can focus on what matters right now."
        ],
        "Self-worth": [
            "I am the mother my children need.",
            "I do not need to prove my value.",
            "I deserve rest, joy and peace."
        ]
    }
    affirmations = affirmations[0] if isinstance (affirmations, tuple) else affirmations

    print("Welcome to the Mini Affirmation Generator")
    print("\nChoose a category:\n")

    for i, category in enumerate(affirmations.keys(), start=1):
        formatted = category.replace("_", "").title()
        print(f"{i}. {formatted}")

    choice = input ("\nEnter your choice: ")

    if choice in affirmations:
        affirmation = random.choice(affirmations[choice])  
        print(f"\n Your affirmation:\n{affirmations}")

    else:
        print("\n Invalid choice. Please try again.")

if __name__ == "__main__": 
    main(   )     