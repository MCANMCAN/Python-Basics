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
#Write your code below this line 👇

rps = ["rock", "paper", "scissors"]

r = 0
p = 1
s = 2

user_input = input("Please select R,S or P !\n").lower()

computer_selection = random.choice(rps)
print("P1\n")
if user_input == 'r':
    selection = rps[r]
    print(rock)
if user_input == 'p':
    selection = rps[r]
    print(paper)
if user_input == 's':
    selection = rps[s]
    print(scissors)
computer_selection = random.choice(rps)
#print(computer_selection)
print("CPU...\n")
if computer_selection == 'rock':
    print(rock)
elif computer_selection == 'paper':
    print(paper)
elif computer_selection == "scissors":
    print(scissors)
# draw scenarios
if user_input == 'r' and computer_selection == 'rock':
    print("Draw!")
if user_input == 'p' and computer_selection == 'paper':
    print("Draw!")
if user_input == 's' and computer_selection == 'scissors':
    print("Draw!")
# winner scenarioes
if user_input == 'r' and computer_selection == 'scissors':
    print("You Won")
elif user_input == 'r' and computer_selection == 'paper':
    print("You lost!")
elif user_input == 'p' and computer_selection == 'rock':
    print("You Won")
elif user_input == 'p' and computer_selection == 'scissors':
    print("You lost!")
elif user_input == 's' and computer_selection == 'rock':
    print("You lost!")
elif user_input == 's' and computer_selection == 'paper':
    print("You Won")
#else:
#  print("Wrong entry, you lost")
