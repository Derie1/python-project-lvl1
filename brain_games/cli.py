import prompt


def welcome_user():
    player = prompt.string('May I have your name? ')
    return f'Hello, {player}'
