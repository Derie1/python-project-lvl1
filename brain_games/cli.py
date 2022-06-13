import prompt


def welcome_user():
    player = prompt.string('May i have your name? ')
    print(f'Hello, {player}')
