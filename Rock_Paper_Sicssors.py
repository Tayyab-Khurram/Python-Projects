import random


def play():
    name = input('Enter your name : ')
    print(f'\nHello {name}! Welcome to Rock Paper Scissors!\n')
    print('You are gonna compete with the computer!')
    user_choice = input("\n'r' for Rock, 's' for Scissors, 'p' for Paper\n\nEnter your choice : ")
    computer = random.choice(['r', 's', 'p'])

    decision(user_choice, computer, name)


def decision(user, computer, name):
    if user == computer:
        only_printing(user, computer, name)
        print('\nIts a tie')

    elif (user == 'r' and computer == 's') or (user == 'p' and computer == 'r') or \
            (user == 's' and computer == 'p'):

        only_printing(user, computer, name)
        print(f'\nTherefore, {name} Won!')

    else:
        only_printing(user, computer, name)
        print('\nTherefore, Computer Won!')


def only_printing(user, computer, name):
    if user == 'r':
        print(f'\n{name}\'s choice : Rock')
    elif user == 's':
        print(f'{name}\'s choice : Scissors')
    if user == 'p':
        print(f'{name}\'s choice : Paper')
    if computer == 'r':
        print('Computer\'s choice : Rock')
    elif computer == 's':
        print('Computer\'s choice : Scissors')
    if computer == 'p':
        print('Computer\'s choice : Paper')


play()          # this is to execute everything written here
