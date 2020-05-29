import random
moves = ['rock', 'paper', 'scissors']
keep_playing = 'True'
while keep_playing == 'True':
    cmove = random.choice(moves)
    pmove = input('what is your move: rock, paper, scissors?')
    print('the computer chose', cmove)
    if cmove == pmove:
        print('Tie')
    elif pmove == 'rock' and cmove == 'scissors':
        print('player wins.')
    elif pmove == 'paper' and cmove == 'rock':
        print('player wins.')
    elif pmove == 'scissors' and cmove == 'paper':
        print('player wins.')
    elif pmove == 'scissors' and cmove == 'rock':
        print('computer wins.')
    elif pmove == 'rock' and cmove == 'paper':
        print('computer wins.')
    elif pmove == 'paper' and cmove == 'scissors':
        print('computer wins')
    else:
        print('COULD NOT COMPUTE INPUT, PLZ PUT THE THREE INPUT YOU WERE TOLD TO PUT?')