#!/usr/bin/env python
import prompt
from random import randint

START_NUMBER = 1
END_NUMBER = 25
TRIES = 3
WRONG_MSG = "is wrong answer ;(. Correct answer was"


def welcome_user():
    player = prompt.string('May I have your name? ')
    return player


def create_progression():
    number = randint(1, 50)
    interval = randint(1, 5)
    stop = number + interval * 10
    progression = list(range(number, stop, interval))
    return progression


def list_to_string(some_list):
    result_string = ''
    for _ in some_list:
        result_string += str(f"{_} ")
    return result_string


def is_corret_answer(players_answer, correct_answer):
    return players_answer == correct_answer


def main():
    user_name = welcome_user()
    print(f'Hello, {user_name}!')
    print('What number is missing in the progression?')
    for _ in range(TRIES):
        progression = create_progression()
        random_index = randint(0, len(progression) - 1)
        correct_answer = str(progression[random_index])
        progression[random_index] = '..'
        question = list_to_string(progression)
        print(f"Question: {question}")
        players_answer = prompt.string('Your answer: ')

        if is_corret_answer(players_answer, correct_answer):
            print('Correct!')
        else:
            print(
                f"'{players_answer}' {WRONG_MSG} '{correct_answer}'")
            print(f"Let's try again, {user_name}!")
            return
    print(f'Congratulations, {user_name}!')


if __name__ == '__main__':
    main()
