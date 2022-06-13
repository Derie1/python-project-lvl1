import prompt


def welcome_user():
    player = prompt.string('May i have your name? ')
    return f'Hello, {player}'
