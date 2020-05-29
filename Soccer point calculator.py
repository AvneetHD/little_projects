wins = input('How many wins do you have?')
draws = input('How many Draws do you have?')
loses = input('How many loses do you have?')

wins = int(wins)
draws = int(draws)
loses = int(loses)

wins = wins * 3
draws = draws
loses = loses - loses
points = wins + draws + loses

print('You have {}'.format(points))
