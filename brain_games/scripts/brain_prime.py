#!/usr/bin/env python
import prompt
from random import randint

START_NUMBER = 1
END_NUMBER = 100
TRIES = 3


def welcome_user():
    player = prompt.string('May I have your name? ')
    return player


def is_prime(n):
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n and n % d != 0:
        d += 2
    return d * d > n


def is_corret_answer(players_answer, correct_answer):
    return players_answer == correct_answer


def main():
    user_name = welcome_user()
    print(f'Hello, {user_name}!')
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    for _ in range(TRIES):
        question = randint(START_NUMBER, END_NUMBER)
        print(f'Question: {question}')
        if is_prime(question):
            correct_answer = 'yes'
        else:
            correct_answer = 'no'
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
