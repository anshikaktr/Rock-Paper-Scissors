from collections import namedtuple
import random

opt_= namedtuple("opt_",['r','p','s'])
options= opt_('rock','paper','scissors')

def start():
    user=input("Enter r for rock, p for paper, s for scissors: ")
    if user == 'r':
        usr_input=options.r
    if user== 'p':
        usr_input= options.p
    if user== 's':
        usr_input= options.s
    comp=random.choice(['rock','paper','scissors'])
    print("Computer's turn: ",comp)
    winner(usr_input,comp)
    

def winner(player,Comp):
    if player==Comp:
        print("TIE")
    elif (player == 'rock' and Comp == 'paper') or (player == 'paper' and Comp == 'scissors') or (\
        player=='scissors' and Comp=='rock'):
        print(Comp,'wins\nYOU LOST :( ' )
    else:
        print(player,"wins\nHURRAY! YOU WON.")

try:
    n= int(input("How many matches? "))
    for i in range(n):
        start()
    print("THE END OF THE GAME")
except Exception as e:
    print(e)
