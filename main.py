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

#Write your code below this line 👇

game = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors "))

if user_choice >= 3 or user_choice < 0:
  print("Invalid number, You lose")
else:
#prints out the user's choice
  print(game[user_choice])

#generates a random number for the computer
  print("Computer chose:")
  com_choice = random.randint(0, 2)
  
  #Outputs the choice of the computer
  print(game[com_choice])
    
  
  #Selects winner
  if user_choice == 0 and com_choice == 1:
    print("you lost, paper wins rock")
  elif user_choice == 1 and com_choice == 0:
    print("You win, Paper wins rock")
  elif user_choice == 2 and com_choice == 1:
    print("You lose, Scissor wins paper")
  elif user_choice == 1 and com_choice == 2:
    print("You win, Scissor wins paper ")
  elif user_choice == 2 and com_choice == 0:
    print("You lose, Rock wins scissors")
  elif user_choice == 0 and com_choice == 2:
    print("You win, Rock wins scissors ")
  else:
    print("its a draw")
  