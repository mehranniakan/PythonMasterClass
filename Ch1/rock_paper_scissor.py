import random

from django.forms.widgets import Input

Choices = ('Rock','Paper','Scissor')
ans = 'y'
counter = 0

def get_user_choice():
    user_choice = input(f'Make Your Choice : {Choices}')
    print(f'Your Choice : {user_choice}')
    return user_choice

def get_computer_choice():
    computer_choice = random.choice(Choices)
    print(f'Computer Choice : {computer_choice}')
    return computer_choice

def judge(user_choice, computer_choice):
    if user_choice == computer_choice:
        print('Result : Draw')

    elif ((user_choice == 'Rock' and computer_choice == 'Scissor') or
          (user_choice == 'Paper' and computer_choice == 'Rock') or
          (user_choice == 'Scissor' and computer_choice == 'Paper')):
        print('Result : You Win')

    else:
        print('Result : You Loose')


def handler():
    judge(get_user_choice(), get_computer_choice())
    print('Thank You')

while ans == 'y':
    counter += 1
    print(f'{counter} Round:')
    handler()
    ans = input('Press Enter to Continue...{y/n} :')
