from random import choice


def play_game(player_choice: str, computer_choice: str) -> int:
    if player_choice == 'paper':
        if computer_choice == 'paper':
            return 0
        if computer_choice == 'stone':
            return 1
        if computer_choice == 'scissors':
            return 2
    if player_choice == 'stone':
        if computer_choice == 'paper':
            return 2
        if computer_choice == 'stone':
            return 0
        if computer_choice == 'scissors':
            return 1
    if player_choice == 'scissors':
        if computer_choice == 'paper':
            return 1
        if computer_choice == 'stone':
            return 2
        if computer_choice == 'scissors':
            return 0


def test_play_game():
    assert play_game('paper', 'paper') == 0
    assert play_game('paper', 'stone') == 1
    assert play_game('paper', 'scissors') == 2
    assert play_game('stone', 'paper') == 2
    assert play_game('stone', 'stone') == 0
    assert play_game('stone', 'scissors') == 1
    assert play_game('scissors', 'scissors') == 0
    assert play_game('scissors', 'paper') == 1
    assert play_game('scissors', 'stone') == 2


if __name__ == '__main__':
    player = input('Choice: paper, stone, scissors: ')
    computer = choice(['paper', 'stone', 'scissors'])
    result = play_game(player, computer)
    print(f'Computer choice: {computer}')
    if result == 1:
        print('Player won')
    elif result == 2:
        print('Computer won')
    else:
        print('Draw')
