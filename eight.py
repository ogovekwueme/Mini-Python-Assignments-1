#!/usr/bin/python3
 
from getpass import getpass

while True:
    print('Rock Paper Scissors game')
    print('----------------------')
    print('1. R for Rock')
    print('2. P for Paper')
    print('3. S for Scissors')
    print('Enter choice R/P/S')
    player1 = getpass('Player\'s one turn:').upper()
    player2 = getpass('Player\'s 2 turn:').upper()

    if player1 == player2:
        print('it is a tie!')
    elif player1 == 'R' and player2 == 'S':
        print('player1 wins!')
    elif player2 == 'R' and player1 == 'S':
        print('player2 wins!')
    elif player1 == 'S' and player2 =='P':
        print('player1 wins!')
    elif player2 == 'S' and player1 == 'P':
        print('player2 wins!')
    elif player1 == 'P' and player2 == 'R':
        print('player1 wins!')
    elif player2 == 'P' and player1 == 'R':
        print('player2 wins!')
    else:
        print('Wrong choice')
    choice = input('Do you want to play again (y/n):')
    if choice .upper() == 'N':
        break


