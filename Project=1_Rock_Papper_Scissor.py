import random
Rules=["""Rock wins against scissor
scissor wins against paper
paper wins against rock
  user_choice + computer_choice =  result
       0            0           =   Draw
       0            1           =   computer win           
       0            2           =   user win
       1            0           =   user win 
       1            1           =   Draw
       1            2           =   computer win
       2            0           =   computer win 
       2            1           =   user win 
       2            2          =   draw
"""]
rock="✊"
paper="✋"
scissor="✌"
game_image=[rock,paper,scissor]
for i in range(3):
    user_choice = int(input("enter you choice : 0 for Rock, 1 for Paper , 2 for Scissor"))
    if user_choice>=3 or user_choice<0:
        print("You are Entered Invalid input , And you loose the Game!!!")
    else:
        print(f"You choose {game_image[user_choice]}")
        computer_choice = random.randint(0, 2)
        print(f"computer choice is {game_image[computer_choice]}")
        if user_choice == computer_choice:
            print("It's a draw ,try again")
        elif computer_choice == 0 and user_choice == 2:
            print("You Lose!!")
        elif user_choice == 0 and computer_choice == 2:
            print("You win")
        elif computer_choice > user_choice:
            print("You Lose!!!")
        elif user_choice > computer_choice:
            print("You win!!!!")