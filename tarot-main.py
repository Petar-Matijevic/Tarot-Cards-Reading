import json
import random

with open('tarot.json') as f:
    data = json.load(f)


def pull_unique_cards(num_cards, suite_choice, upright):
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

        if upright == 4:
            card_interpretation = card_random['interpretation']['normal']
            print("Always Upright card says:", card_interpretation)
        else:
            reversed_card = random.choice([True, False])
            if reversed_card:
                card_interpretation = card_random['interpretation']['reversed']
                print("Reverse card says:", card_interpretation)
            else:
                card_interpretation = card_random['interpretation']['normal']
                print("Upright card says:", card_interpretation)
            print()


def draw_cards():
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

    pull_unique_cards(num_cards_to_pull, suite_choice,0)


def love_spread():
    print("LOVE SPREAD")
    print("#1 - What you currently feel about your relationship, your approach, and your outlook.")
    pull_unique_cards(1, 3,0)  # Pull 1 card representing the user's feelings
    print("#2 - Your partner's current emotions towards you, his attitude, and expectations about your relationship.")
    pull_unique_cards(1, 3,0)  # Pull 1 card representing the partner's emotions
    print("#3 - Common characteristics of both of you")
    pull_unique_cards(1, 3,0)  # Pull 1 card representing common characteristics
    print("#4 - The strength of your relationship.")
    pull_unique_cards(1, 3,0)  # Pull 1 card representing the strength of the relationship
    print("#5 - Weaknesses in your relationship.")
    pull_unique_cards(1, 3,0)  # Pull 1 card representing weaknesses in the relationship
    print("#6 - Your true love card. It interprets if the relationship is going to be successful or not.")
    pull_unique_cards(1, 3,0)  # Pull 1 card representing the true love card

def success_spread():
    print("SUCCESS SPREAD")
    print("#1 - It helps you to find out about the true colors of the challenge in front of you. It will help you to identify what sort of skill set and resources you will need in order to not just solve but also overcome the challenge.")
    pull_unique_cards(1, 3,0)  # Pull 1 card representing the true colors of the challenge
    print("#2 - This further clarifies on your current problems and challenges.")
    pull_unique_cards(1, 3,0)  # Pull 1 card representing current problems and challenges
    print("#3 - The third card reveals the hidden factors affecting your current situation. You need to have knowledge about what these factors are to really overcome the obstacle you’re facing.")
    pull_unique_cards(1, 3,0)  # Pull 1 card representing hidden factors affecting the current situation
    print("#4 - The fourth card represents new plans, people, or objects that can help you grow further. By adapting yourself to these new aspects, your vision of the situation will change, leaving you with better solutions to your problems.")
    pull_unique_cards(1, 3,0)  # Pull 1 card representing new plans, people, or objects for growth
    print("#5 - The final card shows what requirements you need to fulfill in order to be proven successful and things you should avoid as they will lead you to failure. It will point you towards success if proven to be a positive card but in other cases it could be a negative card and will warn you about an upcoming disaster in your life.")
    pull_unique_cards(1, 3,0)  # Pull 1 card representing requirements for success or failure

def celtic_cross_spread():
    print("CELTIC CROSS SPREAD")
    print("#1 - Presents the current situation the person finds themselves in and the reading is about the question they are facing.")
    pull_unique_cards(1, 3,0)  # Pull 1 card representing the current situation
    print("#2 - Is placed over the first card, pointing to the left and is always read in an upright position. It shows what the basic challenge is that needs to be solved or the mental or physical object holding them back.")
    pull_unique_cards(1, 3,4)  # Pull 1 card representing the basic challenge
    print("#3 - The third spread reveals the subconscious influences. These strange influences have an extremely strong and powerful effect on one’s everyday life, especially in scenes relating to the question.")
    pull_unique_cards(1, 3,0)  # Pull 1 card representing subconscious influences
    print("#4 - The fourth card shows what resources one has and the things they can use to face and solve the problem shown by the second card and in the process reach their ultimate goal, shown by the third card.")
    pull_unique_cards(1, 3,0)  # Pull 1 card representing available resources
    print("#5 - The fifth card shows the prologue of the scene. A negatively influenced past may have an effect that prevents their success on their current situation and they will need to let the memory go in order to stop it from negatively influencing their current situation so they can face and eventually overcome the problem at hand as shown by the second card. A positive past should be can simply be called inspiration. Even though the person may be facing a challenge in their current part of life, the problem They are up against is natural growth of the positive past they had the benefit of experiencing and after they have overcome all their challenges, things will look even brighter than they were in the past.")
    pull_unique_cards(1, 3,0)  # Pull 1 card representing past influences
    print("#6 - The sixth card is the headlight. If the card states there is some form of negative energy on the way the five previous cards should give a good reasoning of why this is taking place and what we could do to prevent it.")
    pull_unique_cards(1, 3,0)  # Pull 1 card representing future influences
    print("#7 - The seventh card represents the person’s attitude. It illustrates your physical actions, thinking and ideals regarding the current problem. This will give you more to work with into whether the person’s attitude is conducive to a likable outcome or whether it’s time to retrack the way the person perceives the information.")
    pull_unique_cards(1, 3,0)  # Pull 1 card representing the person's attitude
    print("#8 - The eighth card is an energy card. It talks about the energy surrounding them and the energy other people and the environment is letting off and if these energies are helping in any shape or form.")
    pull_unique_cards(1, 3,0)  # Pull 1 card representing surrounding energies
    print("#9 - The ninth card tells us about what the person’s desires and fears. This is a revelation card. It gives importance to the things a person should be aware of in their current situation and might change the way a person acts which should not be neglected by them.")
    pull_unique_cards(1, 3,0)  # Pull 1 card representing desires and fears
    print("#10 - This is the final outcome and emphasizes on the energies, if they are complementing or conflicting. It also tells the person about the future that will take place immediately and if it is necessary or not to face the future.")
    pull_unique_cards(1, 3,0)  # Pull 1 card representing the final outcome

def spiritual_guidance_spread():
    print("SPIRITUAL GUIDANCE SPREAD")
    print("#1 - The first card represents your main concerns. You may think you know about the problem but this spread goes more in depth with it.")
    pull_unique_cards(1, 3, 0)  # Pull 1 card representing main concerns
    print("#2 - The second card looks into your motivation for looking for guidance.")
    pull_unique_cards(1, 3, 0)  # Pull 1 card representing motivation
    print("#3 - The third card looks into the things about your life you are insecure or worried about.")
    pull_unique_cards(1, 3, 0)  # Pull 1 card representing insecurities or worries
    print("#4 - The fourth card emphasizes on the parts of your life that you are not aware of.")
    pull_unique_cards(1, 3, 0)  # Pull 1 card representing unconscious aspects
    print("#5 - The fifth card is your advice card as it will guide you to the steps to face your fears. It ties in with the previous cards.")
    pull_unique_cards(1, 3, 0)  # Pull 1 card representing advice
    print("#6 - The sixth card guides us to a life with no worries so that we could move forward on our spiritual journey.")
    pull_unique_cards(1, 3, 0)  # Pull 1 card representing a worry-free life
    print("#7 - The seventh card teaches you to deal with the situation with the resources you have at hand.")
    pull_unique_cards(1, 3, 0)  # Pull 1 card representing available resources
    print("#8 - Finally, the eighth card finishes the Spiritual Guidance Spread by telling us that the result of the tarot cards all depends on our reaction to it whether we focus on the positive or negative.")
    pull_unique_cards(1, 3, 0)  # Pull 1 card representing the impact of reaction

def career_path_spread():
    print("CAREER PATH SPREAD")
    print("#1 - The first card asks us if our current job is our ideal job.")
    pull_unique_cards(1, 3, 0)  # Pull 1 card representing current job satisfaction
    print("#2 - The second card emphasizes on the actions we must take to further boost our career.")
    pull_unique_cards(1, 3, 0)  # Pull 1 card representing career boosting actions
    print("#3 - The third card tells us about certain things about our job that we can no longer alter.")
    pull_unique_cards(1, 3, 0)  # Pull 1 card representing unchangeable aspects of the job
    print("#4 - The fourth card refers to our skills on our job to see if they’re enough to get us a promotion.")
    pull_unique_cards(1, 3, 0)  # Pull 1 card representing job skills
    print("#5 - The fifth card tells us about the things we can do in our career to improve.")
    pull_unique_cards(1, 3, 0)  # Pull 1 card representing career improvement options
    print("#6 - The sixth card gives us the answer to the question if our past mistakes are influencing our career now.")
    pull_unique_cards(1, 3, 0)  # Pull 1 card representing influence of past mistakes
    print("#7 - The final card tells you that if the card is negative it might lead to a bad outcome.")
    pull_unique_cards(1, 3, 0)  # Pull 1 card representing potential career outcomes


while True:
    choice = input(
        "Do you want to perform a Love Spread (L), Success Spread (S), Celtic Cross (C), Spiritual Guidance Spread (I), Career Path (P) or just draw cards (D)?  Or end the session (B) ").upper()
    if choice == 'L':
        love_spread()
    elif choice == 'S':
        success_spread()
    elif choice == 'C':
        celtic_cross_spread()
    elif choice == 'I':
        spiritual_guidance_spread()
    elif choice == 'P':
        career_path_spread()
    elif choice == 'D':
        draw_cards()
    elif choice == 'B':
        break
    else:
        print("Invalid choice. Please enter the respective letter of your choice.")

