import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print("Welcome to The Rock, Paper, Scissors Game!\n")
game_choice = [rock, paper, scissors]

my_choice = int(input("What do you choose? Type '0' for Rock, '1' for Paper or '2' for Scissors.\n"))

if 0 <= my_choice <=2:
    print(f"You Chose:\n{game_choice[my_choice]}")

    computer_choice = random.randint(0, 2)
    print(f"Computer Chose:\n{game_choice[computer_choice]}")

    if my_choice == computer_choice:
        print("It's a Draw\nGame Over!")

    elif my_choice == 0 and computer_choice == 2:
        print("Congrats! You win")

    elif my_choice == 2 and computer_choice == 1:
        print("Congrats! You win")

    elif my_choice == 1 and computer_choice == 0:
        print("Congrats! You win")

    else:
        print("Oh no! You lose")

else:
    print("You typed an invalid number. You lose")
