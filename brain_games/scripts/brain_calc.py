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


def calculate(first_operand, second_operand, operator):
    if operator == '+':
        return first_operand + second_operand
    elif operator == '-':
        return first_operand - second_operand
    elif operator == '*':
        return first_operand * second_operand


def is_corret_answer(players_answer, correct_answer):
    return players_answer == correct_answer


def main():
    user_name = welcome_user()
    print(f'Hello, {user_name}!')
    print('What is the result of the expression?')
    signs = ('+', '-', '*')
    for _ in range(TRIES):
        number1 = randint(START_NUMBER, END_NUMBER)
        number2 = randint(START_NUMBER, END_NUMBER)
        operator = signs[randint(0, 2)]
        print(f'Question: {number1} {operator} {number2}')
        correct_answer = str(calculate(number1, number2, operator))
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
