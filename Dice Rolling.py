import random

while True:
    dies = input('How many dies do you want to be rolled?')
    dies = int(dies)
    numbers = [1, 2, 3, 4, 5, 6]
    die1 = random.choice(numbers)
    die2 = random.choice(numbers)
    die3 = random.choice(numbers)
    die4 = random.choice(numbers)
    die5 = random.choice(numbers)
    die6 = random.choice(numbers)
    die7 = random.choice(numbers)
    die8 = random.choice(numbers)
    die9 = random.choice(numbers)
    die10 = random.choice(numbers)

    if dies == 1:
        print('The die(s) rolled a %i' % die1)
    if dies == 2:
        print('The die(s) rolled a %i' % die1, die2)
    if dies == 3:
        print('The die(s) rolled a %i' % die1, die2, die3)
    if dies == 4:
        print('The die(s) rolled a %i' % die1, die2, die3, die4)
    if dies == 5:
        print('The die(s) rolled a %i' % die1, die2, die3, die4, die5)
    if dies == 6:
        print('The die(s) rolled a %i' % die1, die2, die3, die4, die5, die6)
    if dies == 7:
        print('The die(s) rolled a %i' % die1, die2, die3, die4, die5, die6, die7)
    if dies == 8:
        print('The die(s) rolled a %i' % die1, die2, die3, die4, die5, die6, die7, die8)
    if dies == 9:
        print('The die(s) rolled a %i' % die1, die2, die3, die4, die5, die6, die7, die8
              , die9)
    if dies == 10:
        print('The die(s) rolled a %i' % die1, die2, die3, die4, die5, die6, die7
              , die8, die9, die10)
