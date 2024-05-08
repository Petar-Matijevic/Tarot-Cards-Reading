import json
import random

with open('tarot.json') as f:
    data = json.load(f)

def pull_unique_cards(num_cards, suite_choice):
    pulled_cards = []

    for _ in range(num_cards):
        while True:
            # Choose a random card data based on suite choice
            if suite_choice == 1:
                cards_of_suite = [card for card in data['tarot'] if card['suite'] == 'major']
            elif suite_choice == 2:
                cards_of_suite = [card for card in data['tarot'] if card['suite'] == 'minor']
            elif suite_choice == 3:
                cards_of_suite = data['tarot']
            else:
                print("Invalid suite choice. Please try again.")
                return

            card_random = random.choice(cards_of_suite)

            name_card = card_random['name']
            if name_card not in pulled_cards:
                pulled_cards.append(name_card)
                break

        print("Universe smiles upon you, my child")
        print("Card:", name_card)
        print("Suite:", card_random['suite'])
        print("Card reveals:", card_random['description'])

        reversed_card = random.choice([True, False])
        if reversed_card:
            card_interpretation = card_random['interpretation']['reversed']
            print("Reverse card says:", card_interpretation)
        else:
            card_interpretation = card_random['interpretation']['normal']
            print("Upright card says:", card_interpretation)
        print()

while True:
    num_cards_to_pull = input("How many cards do you want to pull out? ")
    if num_cards_to_pull.isdigit():
        num_cards_to_pull = int(num_cards_to_pull)
        if num_cards_to_pull > 0:
            break
        else:
            print("Please enter a number greater than zero.")
    else:
        print("Please enter a valid positive integer.")

# User input for suite choice
print("Please choose a suite:")
print("1. Major Arcana")
print("2. Minor Arcana")
print("3. Both Major and Minor Arcana")

while True:
    suite_choice = input("Enter your choice (1/2/3): ")
    if suite_choice.isdigit():  # Check if input is a digit
        suite_choice = int(suite_choice)
        if suite_choice in [1, 2, 3]:  # Check if input is one of the valid choices
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
    else:
        print("Invalid input. Please enter a number.")

pull_unique_cards(num_cards_to_pull, suite_choice)