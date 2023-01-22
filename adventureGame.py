# Sunday night fun time - adventure game 

# import modules
import time

# Ask user for their name
userName = input("What is your name?\n")

# Welcome user to the game
print(f"Great to have you on board, {userName}. Enjoy the walk!")

# Make the game a bit more user-friendly by delaying prompt display in terminal
time.sleep(2)


while True: 
    # First question
    answerOne = input(f"You're hydrated, walking in a forest. You slept well so you've been walking all day long until the evening. You feel weird - you ask yourself: 'Did I walk here yesterday?!?'. You can go 'left' or 'right'. Shall we go 'left' or 'right', {userName}?\n").lower()

    # Survival scenario
    if answerOne == "left":

        answerTwo = input("Good choice! You come to a small house, which seems empty. You can 'get inside' or 'burn the house'. What would you like to do?\n").lower()

        # Survival scenario
        if answerTwo == "burn the house":
            print("Great idea! The house was full of zombies! They try to get out but you manage to escape.\n")

            answerThree = input("All that fire makes the forest bright and you find a way back home, but you're very hungry. 'McDonalds' or 'takeaway'?\n").lower()

            # Game over scenario
            if answerThree == "mcdonalds": 
                print("McDonalds is now a Zombie venue where you are their fast food! And now you're dead too! Enjoy zombie life. Game over.\n ")
                break
            
            # Game over scenario
            elif answerThree == 'takeaway':
                print("You wait and wait, but the takeway food doesn't arrive and you die out of hunger. Try drinking cola in your next life? It was in the fridge. At least you're not a zombie. Game over! \n")
                break

            else: 
                print(f"{answerThree} is not a possibility. A zombie approached you as you hesitated and now you're dead too! Enjoy zombie life. Game over.\n")
                break

        # Game over scenario
        elif answerTwo == "get inside": 
            print(f"Sorry, {userName}. Turns out the house isn't empty. It's full of zombies and now you're dead too. Enjoy zombie life. Game over!")
            break

        # Game over scenario
        else:
            print(f"{answerTwo} is not a possibility. A zombie approached you as you hesitated and now you're dead too! Enjoy zombie life. Game over.\n")
            break

    # Survival scenario
    elif answerOne == "right": 

        answerTwo = input("You see an animal in a distance, but it's very dark. Should we 'approach' or 'run away'?\n").lower()

        # Survival scenario
        if answerTwo == "approach":
            
            answerThree = input("It's a friendly dog! It helps you get out of the forest. You get home and decide to drink something. 'Cola' or 'water'?\n").lower()
            
            # Game over scenario
            if answerThree == "cola": 
                print("All the cola stock in your city was poisoned with a radioactive substance. You turn into a zombie and now you're dead too. Enjo zombie life. Game over.\n")
                break
            
            # Back to the first question in the forest for another walk in the forest
            elif answerThree == 'water': 
                print('You go to sleep and dream about zombies in the forest. Well, at least you are not a zombie yourself. You decide to go for a walk... in a forest (yikes!).\n')

                for i in range(5):
                    time.sleep(2)
                    print(".", end=" ", flush=True)
                    
                
                print("\n")
                continue
            
            # Game over scenario
            else: 
                print(f"{answerThree} is not a possibility. A zombie approached you as you hesitated and now you're dead too! Enjoy zombie life. Game over.\n")
                break

        elif answerTwo == "run away":

            # Game over scenario
            print("A group of jogging zombies see you running and decide to join you. When they realise you're not a zombie they eat you and now you're dead too. Enjoy zombie life. Game over.\n")
            break

        # Game over scenario
        else: 
            print(f"{answerTwo} is not a possibility. A zombie approached you as you hesitated and now you're dead too! Enjoy zombie life. Game over.\n")
            break

    # Game over scenario
    else: 
        print(f"{answerOne} is not a possibility. A zombie approached you as you hesitated and now you're dead too! Enjoy zombie life. Game over.\n")
        break

# Decoration before final message
for i in range(5):
    time.sleep(1)
    print(".", end=" ", flush=True)

# Thank user for playing
print("\nThanks for playing!")


# Made with love.
# Check out Harry Mack on YouTube. 
# Have a great day.