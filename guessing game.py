import random
import time

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
num1 = random.randint(10, 50)
num2 = random.choice(x)
num3 = num1 - num2
tries = 5
while tries >= 1:
    print('You have %i many more tries to guess the number' % tries)
    guess = input('Number please:')
    i = int(guess)
    if i == num1:
        print('Yeah you got it right!')
        break
    else:
        print('that is incorrect please try again.')
        tires = tries - 1
    if tires <= 3:
        print('It is close to %i' % num3)
if tries == 0:
    print('you were unable to guess the number')
    time.sleep(1)
