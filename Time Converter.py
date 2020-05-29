def minutes_to_seconds(x):
    x = int(x)
    x = x * 60

    print('{} seconds.'.format(x))


def hours_to_seconds(x):
    x = int(x)
    x = (x * 60) * 60
    print('{} seconds'.format(x))


direction = input('Do you want to convert hours to seconds. Y/N.')
direction2 = input('Do you want to convert minutes to seconds. Y/N.')

if direction == 'Y' or direction == 'yes':
    hours = input('')
    hours_to_seconds(hours)
if direction2 == 'Y' or direction == 'yes':
    minutes = input('')
    minutes_to_seconds(minutes)
