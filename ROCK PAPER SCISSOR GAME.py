#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      mukes
#
# Created:     23/08/2023
# Copyright:   (c) mukes 2023
# Licence:     <your licence>
print("WELCOME YOUR'S IN [ROCK,PAPER,SCISSOR] GAME")

computer=[0,1,2]
user_choice=int(input('''Enter your choice
0/1/2
0-rock
1-paper
2-scissor

user_choice '''))
import random

# Selecting random choice
bot_choice= random.choice(computer)
print( "bot_choice" ,bot_choice)
if user_choice==0:
    if bot_choice==2:
        print("hurray you won the game")
    elif bot_choice==1:
        print("bad luck !, you lose the game")
    elif bot_choice==0:
        print("draw!")
elif user_choice==1:
    if bot_choice==0:
        print("hurray you won the game")
    elif bot_choice==2:
        print("bad luck !, you lose the game")
    elif bot_choice==1:
        print("draw!")
elif user_choice==2:
    if bot_choice==1:
        print("hurray you won the game")
    elif bot_choice==0:
        print("bad luck !, you lose the game")
    elif bot_choice==2:
        print("draw!")
else:
    print("Invalid Input ")


