import random
import time


name = input('Enter your name:')
time.sleep(1)
print('welcome %s to a game of HangMan made by Avneet' % name)
time.sleep(1.5)
print('instructions:')
time.sleep(0.5)
print('this is a really early version of the game so sorry if there is some problems in the function of the game.')
time.sleep(2.5)
print('when playing this game make sure you only put one letter at a time and to put no spaces or capital letter and')
time.sleep(2.5)
print('or making a new line to type your guess.')
time.sleep(1)
print('please be patient with the game, and most importantly of all have FUN!!!')
time.sleep(1.5)
fruits = ['apple', 'orange', 'banana', 'grapes', 'apricots', 'raspberry', 'blueberry', 'raisins', 'kiwi', 'tablet',
          'iphone', 'Samsung', 'Pc', 'laptop', 'technology', 'fitbit', 'monday', 'tuesday', 'wednesday', 'thursday',
          'friday', 'saturday', 'sunday', 'january', 'february', 'march', 'april', 'may', 'june', 'july', 'december',
          'november', 'october', 'september', 'name']
word = random.choice(fruits)
word1 = word + '.'
length = len(word)
display = '*' * length
limit = 6

while 1 <= limit <= 6:
    print('number of guesses: %i' % limit)
    time.sleep(1)
    guess = input('The word is ' + display + '.What is your guess?')
    time.sleep(1)
    if guess in word:
        print('%s is in the word.' % guess)
        index = word.find(guess)
        word = word[:index] + '*' + word[index + 1:]
        display = display[:index] + guess + display[index + 1:]
    else:
        print('No, %s is not in the word' % guess)
        limit = limit - 1
        if limit == 6:
            print(' ________\n'
                  ' l      l\n'
                  ' l      \n'
                  ' l\n'
                  ' l\n'
                  ' l\n'
                  ' l\n'
                  '_l_\n')
        if limit == 5:
            print(' ________\n'
                  ' l      l\n'
                  ' l      o\n'
                  ' l      \n'
                  ' l\n'
                  ' l\n'
                  ' l\n'
                  '_l_\n')
        if limit == 4:
            print(' ________\n'
                  ' l      l\n'
                  ' l      o\n'
                  ' l      l\n'
                  ' l\n'
                  ' l\n'
                  ' l\n'
                  '_l_\n')
        if limit == 3:
            print(' ________\n'
                  ' l      l\n'
                  ' l      o\n'
                  ' l     /l \n'
                  ' l\n'
                  ' l\n'
                  ' l\n'
                  '_l_\n')
        if limit == 2:
            print(' ________\n'
                  ' l      l\n'
                  ' l      o\n'
                  ' l     /l\ \n'
                  ' l     \n'
                  ' l\n'
                  ' l\n'
                  '_l_\n')
        if limit == 1:
            print(' ________\n'
                  ' l      l\n'
                  ' l      o\n'
                  ' l     /l\ \n'
                  ' l     /\n'
                  ' l\n'
                  ' l\n'
                  '_l_\n')
        if limit == 0:
            print(' ________\n'
                  ' l      l\n'
                  ' l      o\n'
                  ' l     /l\ \n'
                  ' l     / \ \n'
                  ' l\n'
                  ' l\n'
                  '_l_\n')

    if word == '*' * length:
        print('Congratulations you won, %s is the word' % display)
        print('Thanks for playing')
        break
    elif limit == 0:
        print('You have run out of guesses, the word was %s' % word1)
        print('Thanks for playing')
        break
