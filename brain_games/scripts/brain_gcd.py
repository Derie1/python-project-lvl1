#!/usr/bin/env python
import prompt
from random import randint
import math

START_NUMBER = 1
END_NUMBER = 100
TRIES = 3


def welcome_user():
    player = prompt.string('May I have your name? ')
    return player


def get_gcd(num1, num2):
    return math.gcd(num1, num2)


def is_corret_answer(players_answer, correct_answer):
    return players_answer == correct_answer


def main():
    user_name = welcome_user()
    print(f'Hello, {user_name}!')
    print('Find the greatest common divisor of given numbers.')
    for _ in range(TRIES):
        number1 = randint(START_NUMBER, END_NUMBER)
        number2 = randint(START_NUMBER, END_NUMBER)
        print(f'Question: {number1} {number2}')
        correct_answer = str(get_gcd(number1, number2))
        players_answer = prompt.string('Your answer: ')

        if is_corret_answer(players_answer, correct_answer):
            print('Correct!')
        else:
            print(
                f"'{players_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'")
            print(f"Let's try again, {user_name}!")
            return
    print(f'Congratulations, {user_name}!')


if __name__ == '__main__':
    main()
