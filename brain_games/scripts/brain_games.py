#!/usr/bin/env python
from brain_games.cli import welcome_user


def main():
    print('Welcome to the Brain Games!')
    user_name = welcome_user()
    print(user_name)


if __name__ == '__main__':
    main()
