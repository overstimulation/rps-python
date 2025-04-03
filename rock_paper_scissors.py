import random

options = {1: 'Rock ✊', 2: 'Paper ✋', 3: 'Scissors ✌️', 4: 'Lizard 🦎', 5: 'Spock 🖖'}
winning_combinations = {
    1: [3, 4],  # Rock beats Scissors, Lizard
    2: [1, 5],  # Paper beats Rock, Spock
    3: [2, 4],  # Scissors beats Paper, Lizard
    4: [2, 5],  # Lizard beats Paper, Spock
    5: [1, 3]   # Spock beats Rock, Scissors
}
advanced_mode = 0

while True:
    print('\n===================')
    print('Rock Paper Scissors')
    print('===================')
    print(f'[1] {options[1]}\n[2] {options[2]}\n[3] {options[3]}')

    player = int(input('🤔 Pick a number: '))

    while player not in range(1,4):
        print('\n⚠️ Invalid input, pick a number from 1 to 3')
        player = int(input('🤔 Pick a number: '))

    computer = random.randint(1,3)
    print(f'\nYou chose: {options[player]}\nCPU chose: {options[computer]}')

    if player == computer:
        print('It\'s a tie! ⚖️')
    elif computer in winning_combinations[player]:
        print('The player won! 🎉')
        print('Congratulations! 🏆 Do you want to play the advanced version now? 🚀\n[1] Yes ✅\n[2] No  ❌')
        go_advanced = int(input('Pick a number: '))
        if go_advanced == 1:
            advanced_mode = 1
            break
    else:
        print('The CPU won! 🤖')

    print('\nDo you want to play again? 🎮\n[1] Yes ✅\n[2] No  ❌')
    rematch = int(input('Pick a number: '))

    while rematch not in range(1,3):
        print('\n⚠️ Invalid input, pick either 1 (Yes) or 2 (No)')
        rematch = int(input('🤔 Pick a number: '))

    if rematch == 2:
        print('\nThanks for playing, see you again next time! 👋')
        break

while advanced_mode == 1:
    print('\n================================')
    print('Rock Paper Scissors Lizard Spock')
    print('================================')
    print(f'[1] {options[1]}\n[2] {options[2]}\n[3] {options[3]}\n[4] {options[4]}\n[5] {options[5]}')

    player = int(input('🤔 Pick a number: '))

    while player not in range(1,6):
        print('\n⚠️ Invalid input, pick a number from 1 to 5')
        player = int(input('🤔 Pick a number: '))

    computer = random.randint(1,5)
    print(f'\nYou chose: {options[player]}\nCPU chose: {options[computer]}')

    if player == computer:
        print('It\'s a tie! ⚖️')
    elif computer in winning_combinations[player]:
        print('The player won! 🎉')
    else:
        print('The CPU won! 🤖')

    print('\nDo you want to play again? 🎮\n[1] Yes ✅\n[2] No  ❌')
    rematch = int(input('Pick a number: '))

    while rematch not in range(1,3):
        print('\n⚠️ Invalid input, pick either 1 (Yes) or 2 (No)')
        rematch = int(input('🤔 Pick a number: '))

    if rematch == 2:
        print('\nThanks for playing, see you again next time! 👋')
        break