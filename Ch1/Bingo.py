import random

max_num = 10
min_num = 1


def get_user_guess():
    while True:
        try:
            return int(input("Enter a number between 1 and 10: "))
        except ValueError:
            print("Please enter a valid number!!!!!!")


def make_random_number():
    return random.randint(min_num, max_num)



def judge():
    guess_count = 3

    guess = get_user_guess()
    goal = make_random_number()

    while guess != goal or guess_count > 0:

        guess_count -= 1

        if guess == goal:
            print(f"You won! The number was {guess}")
            break
        elif guess_count == 0:
            print(f"You have run out of guesses !! the correct number was {goal}")
            break
        else:
            guess = get_user_guess()


judge()