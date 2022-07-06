#!/usr/bin/env python
import prompt
from random import randint

START_NUMBER = 1
END_NUMBER = 99
TRIES = 3


def welcome_user():
    player = prompt.string('May i have your name? ')
    return player


def is_even(x):
    return x % 2 == 0


def main():
    print('Welcome to the Brain Even Game!')
    user_name = welcome_user()
    print(f'Hello, {user_name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for _ in range(TRIES):
        number = randint(START_NUMBER, END_NUMBER)
        print(f'Question: {number}')
        players_answer = prompt.string('Your answer: ')
        if (is_even(number) and players_answer == 'yes') or (
                not is_even(number) and players_answer == 'no'):
            print('Correct!')
        elif is_even(number) and players_answer == 'no':
            print("'no' is wrong answer ;(. Correct answer was 'yes'.")
            print(f"Let's try again, {user_name}!")
            return
        elif not is_even(number) and players_answer == 'yes':
            print("'yes' is wrong answer ;(. Correct answer was 'no'.")
            print(f"Let's try again, {user_name}!")
            return
    print(f'Congratulations, {user_name}!')


if __name__ == '__main__':
    main()
