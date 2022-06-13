#!/usr/bin/env python
import prompt


def welcome_user():
    player = prompt.string('May i have your name? ')
    return f'Hello, {player}'


def main():
    print('Welcome to the Brain Even Game!')
    user_name = welcome_user()
    print(user_name)


if __name__ == '__main__':
    main()
