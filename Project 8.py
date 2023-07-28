#Rock, Paper and Scissors
import random
rock = '''      _______
  ---'   ____)
        (_____)
        (_____)
        (____)
  ---.__(___)

'''
paper = '''      _______
  ---'   ____)____
            ______)
            _______)
           _______)
  ---.__________)
'''
scissors = '''      _______
  ---'   ____)____
            ______)
         __________)
        (____)
  ---.__(___) '''
images = [rock, paper, scissors]

user_choice = int(input("What do you chosse? Type 0 for Rock, 1 for Paper or 2 for Scissors. : \n" ))
print(images[user_choice])


comp_choice = random.randint(0,2)
print(f"Computer chose:")
print(images[comp_choice])

if comp_choice == 0 and user_choice == 2:
    print("You lose!")
elif comp_choice == 2 and user_choice == 0:
    print("You win!")
elif user_choice >= 3 or user_choice < 0:
    print("That move is invalid!, you lose.")
elif comp_choice < user_choice: 
    print("You win!")
elif comp_choice > user_choice: 
    print("You lose!")
elif comp_choice == user_choice:
    print("It's a draw.")