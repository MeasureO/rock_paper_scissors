import random
name = input('Enter your name: ')
print(f'Hello, {name}')
moves = input()
print("Okay, let's start")
def input_answer(options):
    while True:
            user_answer = input()
            if user_answer in options + ['!exit', '!rating']:
                break
            else:
                print('Invalid input')
                continue
    return user_answer 

with open('rating.txt', 'r') as data_file:
    table = [line.strip().split() for line in data_file.readlines()]
    rating = 0
    for row in table:
        if name == row[0]:
            rating = int(row[1])

if moves == '':
    options = ['scissors', 'rock', 'paper']
    while True:
        user_answer = input_answer(options)
        computer_answer = random.choice(options)
        if user_answer == '!rating':
            print(f'Your rating: {rating}')
        elif user_answer == '!exit':
            print('Bye!')
            break
        elif user_answer == computer_answer:
            print(f'There is a draw ({user_answer})')
            rating += 50
        elif user_answer == 'scissors' and computer_answer == 'rock' or user_answer == 'paper' and computer_answer == 'scissors' or user_answer == 'rock' and computer_answer == 'paper':
            print(f'Sorry, but the computer chose {computer_answer}')
        else:
            print(f'Well done. The computer chose {computer_answer} and failed')
            rating += 100
else:
    moves = moves.split(',')
    moves_dict = {}
    for i in range(len(moves)):
        if i != len(moves) - 1:
            moves_dict[moves[i]] = moves[i + 1:] + moves[:i]
        else:
            moves_dict[moves[i]] = moves[:-1]
    while True:
        user_answer = input_answer(moves)
        computer_answer = random.choice(moves)
        if user_answer == '!rating':
            print(f'Your rating: {rating}')
        elif user_answer == '!exit':
            print('Bye!')
            break
        elif user_answer == computer_answer:
            print(f'There is a draw ({user_answer})')   
            rating += 50
        elif computer_answer in moves_dict[user_answer][len(moves_dict[user_answer]) // 2:]:
            print(f'Well done. The computer chose {computer_answer} and failed')
            rating += 100
        else:
            print(f'Sorry, but the computer chose {computer_answer}')