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

import random

rock_paper_scissors = [rock, paper, scissors]
random_indexes = random.randint(0, 2)
your_choice = int(input("What do you choose ? Type 0 for Rock, 1 for Paper and 2 for Scissors "))
computer_choice = rock_paper_scissors[random_indexes]

if your_choice == 0:
    print(rock_paper_scissors[0])
elif your_choice == 1:
    print(rock_paper_scissors[1])
else:
    print(rock_paper_scissors[2])

print(f"Computer chose: \n {computer_choice}")

if computer_choice == rock_paper_scissors[0]:
    if your_choice == 0:
        print("It's a Tie. Play Again!")
    elif your_choice == 1:
        print("You Won. Play Again")
    else:
        print("You Lose. Play Again!")
elif computer_choice == rock_paper_scissors[1]:
    if your_choice == 0:
        print("You Lose. Play Again!")
    elif your_choice == 1:
        print("It's a Tie. Play Again")
    else:
        print("You Won. Play Again!")
elif computer_choice == rock_paper_scissors[2]:
    if your_choice == 0:
        print("You Won. Play Again!")
    elif your_choice == 1:
        print("You Lose. Play Again")
    else:
        print("It's a Tie. Play Again!")
### END OF CODE ###