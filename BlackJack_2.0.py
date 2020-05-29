import random
import time
card_num = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
suites = ['Diamonds', 'Hearts', 'Spades', 'Clubs']

direction = '3'

while direction == '3' or direction == '2':

    def Decison_1(Pmove, Pcard1_num, Pcard2_num, Pcard3_num, Player_end_value, Dcard1, Dcard1_num, Dcard2, Dcard2_num,
                  Dcard3, Dcard3_num, Dcard4, Dcard4_num, Dcrad5, Dcard5_num, Dealer_end_value):
        Player_end_value = Pcard1_num + Pcard2_num

        if 'hit' in Pmove:
            time.sleep(1)
            print('You got the {0}'.format(Pcard3))
            Player_end_value = Player_end_value + Pcard3_num

        if 'stand' in Pmove:
            time.sleep(1)
            print("Okay now it is the dealer's turn, lets see what it does.")
            time.sleep(1)
            Dealers_end_value = Dcard1_num + Dcard2_num

            if Dealers_end_value <= 17:
                print('The dealer chose to hit and got the {0}'.format(Dcard3))
                print('Dealers cards:')
                print(Dcard1)
                print(Dcard2)
                print(Dcard3)
                Dealers_end_value = Dealers_end_value + Dcard3_num
                time.sleep(1)

            if Dealers_end_value >= 17:
                print('The dealer chose to stand')
                time.sleep(1)

                if Dealers_end_value <= 21 and Player_end_value <= 21:
                    if Dealers_end_value > Player_end_value:
                        print('You lost')
                    else:
                        print('You won')
                else:
                    if Dealers_end_value > 21:
                        print('The Dealer busted you win')
                    if Player_end_value > 21:
                        print('You busted and the Dealer won')

                if Dealers_end_value <= 17:
                    print('The dealer chose to hit and got the {0}'.format(Dcard4))
                    print('Dealers cards:')
                    print(Dcard1)
                    print(Dcard2)
                    print(Dcard3)
                    print(Dcard4)
                    Dealers_end_value = Dealers_end_value + Dcard4_num
                    time.sleep(1)

                if Dealers_end_value >= 17:
                    print('The dealer chose to stand')
                    time.sleep(1)
                    if Dealers_end_value <= 21 and Player_end_value <= 21:
                        if Dealers_end_value > Player_end_value:
                            print('You lost')
                        else:
                            print('You won')
                    else:
                        if Dealers_end_value > 21:
                            print('The Dealer busted you win')
                        if Player_end_value > 21:
                            print('You busted and the Dealer won')

                    if Dealers_end_value <= 17:
                        print('The dealer chose to hit and got the {0}'.format(Dcard5))
                        print('Dealers cards:')
                        print(Dcard1)
                        print(Dcard2)
                        print(Dcard3)
                        print(Dcard4)
                        print(Dcard5)
                        Dealers_end_value = Dealers_end_value + Dcard5_num
                        time.sleep(1)
                        print('The dealer chose to stand')
                        time.sleep(1)
                        if Dealers_end_value <= 21 and Player_end_value <= 21:
                            if Dealers_end_value > Player_end_value:
                                print('You lost')
                            else:
                                print('You won')
                        else:
                            if Dealers_end_value > 21:
                                print('The Dealer busted you win')
                            if Player_end_value > 21:
                                print('You busted and the Dealer won')

                    if Dealers_end_value > 17:
                        print('The Dealer chose to stand')
                        time.sleep(1)
                        if Dealers_end_value <= 21 and Player_end_value <= 21:
                            if Dealers_end_value > Player_end_value:
                                print('You lost')
                            else:
                                print('You won')
                        else:
                            if Dealers_end_value > 21:
                                print('The Dealer busted you win')
                            if Player_end_value > 21:
                                print('You busted and the Dealer won')

    Pcard1_suite = random.choice(suites)
    Pcard1_random_num = random.choice(card_num)
    Pcard1 = "'{0}','{1}'".format(Pcard1_random_num, Pcard1_suite)
    Pcard2_suite = random.choice(suites)
    Pcard2_random_num = random.choice(card_num)
    Pcard2 = "'{0}', '{1}'".format(Pcard2_random_num, Pcard2_suite)
    Pcard3_suite = random.choice(suites)
    Pcard3_random_num = random.choice(card_num)
    Pcard3 = "'{0}', '{1}'".format(Pcard3_random_num, Pcard3_suite)
    Pcard4_suite = random.choice(suites)
    Pcard4_random_num = random.choice(card_num)
    Pcard4 = "'{0}', '{1}'".format(Pcard4_random_num, Pcard4_suite)
    Pcard5_suite = random.choice(suites)
    Pcard5_random_num = random.choice(card_num)
    Pcard5 = "'{0}', '{1}'".format(Pcard5_random_num, Pcard5_suite)

    Dcard1_suite = random.choice(suites)
    Dcard1_random_num = random.choice(card_num)
    Dcard1 = "'{0}', '{1}'".format(Dcard1_random_num, Dcard1_suite)
    Dlen = len(Dcard1)
    D_censored = '*' * Dlen
    Dcard2_suite = random.choice(suites)
    Dcard2_random_num = random.choice(card_num)
    Dcard2 = "'{0}', '{1}'".format(Dcard2_random_num, Dcard2_suite)
    Dcard3_suite = random.choice(suites)
    Dcard3_random_num = random.choice(card_num)
    Dcard3 = "'{0}', '{1}'".format(Dcard3_random_num, Dcard3_suite)
    Dcard4_suite = random.choice(suites)
    Dcard4_random_num = random.choice(card_num)
    Dcard4 = "'{0}', '{1},".format(Dcard4_random_num, Dcard4_suite)
    Dcard5_suite = random.choice(suites)
    Dcard5_random_num = random.choice(card_num)
    Dcard5 = "'{0}', '{1}'".format(Dcard5_random_num, Dcard5_suite)

    if '2' in Pcard1:
        Pcard1_num = 2
    if '3' in Pcard1:
        Pcard1_num = 3
    if '4' in Pcard1:
        Pcard1_num = 4
    if '5' in Pcard1:
        Pcard1_num = 5
    if '6' in Pcard1:
        Pcard1_num = 6
    if '7' in Pcard1:
        Pcard1_num = 7
    if '8' in Pcard1:
        Pcard1_num = 8
    if '9' in Pcard1:
        Pcard1_num = 9
    if '10' in Pcard1:
        Pcard1_num = 10
    if 'J' in Pcard1:
        Pcard1_num = 10
    if 'Q' in Pcard1:
        Pcard1_num = 10
    if 'K' in Pcard1:
        Pcard1_num = 10
    if 'A' in Pcard1:
        Poo = input('Do you want to make your ace a 1 or 11?')
        Pcard1_num = int(Poo)

    if '2' in Pcard2:
        Pcard2_num = 2
    if '3' in Pcard2:
        Pcard2_num = 3
    if '4' in Pcard2:
        Pcard2_num = 4
    if '5' in Pcard2:
        Pcard2_num = 5
    if '6' in Pcard2:
        Pcard2_num = 6
    if '7' in Pcard2:
        Pcard2_num = 7
    if '8' in Pcard2:
        Pcard2_num = 8
    if '9' in Pcard2:
        Pcard2_num = 9
    if '10' in Pcard2:
        Pcard2_num = 10
    if 'J' in Pcard2:
        Pcard2_num = 10
    if 'Q' in Pcard2:
        Pcard2_num = 10
    if 'K' in Pcard2:
        Pcard2_num = 10
    if 'A' in Pcard2:
        Poo = input('Do you want to make your ace a 1 or 11?')
        Pcard2_num = int(Poo)

    if '2' in Dcard1:
        Dcard1_num = 2
    if '3' in Dcard1:
        Dcard1_num = 3
    if '4' in Dcard1:
        Dcard1_num = 4
    if '5' in Dcard1:
        Dcard1_num = 5
    if '6' in Dcard1:
        Dcard1_num = 6
    if '7' in Dcard1:
        Dcard1_num = 7
    if '8' in Dcard1:
        Dcard1_num = 8
    if '9' in Dcard1:
        Dcard1_num = 9
    if '10' in Dcard1:
        Dcard1_num = 10
    if 'J' in Dcard1:
        Dcard1_num = 10
    if 'Q' in Dcard1:
        Dcard1_num = 10
    if 'K' in Dcard1:
        Dcard1_num = 10

    if '2' in Dcard2:
        Dcard2_num = 2
    if '3' in Dcard2:
        Dcard2_num = 3
    if '4' in Dcard2:
        Dcard2_num = 4
    if '5' in Dcard2:
        Dcard2_num = 5
    if '6' in Dcard2:
        Dcard2_num = 6
    if '7' in Dcard2:
        Dcard2_num = 7
    if '8' in Dcard2:
        Dcard2_num = 8
    if '9' in Dcard2:
        Dcard2_num = 9
    if '10' in Dcard2:
        Dcard2_num = 10
    if 'J' in Dcard2:
        Dcard2_num = 10
    if 'Q' in Dcard2:
        Dcard2_num = 10
    if 'K' in Dcard2:
        Dcard2_num = 10

    if '2' in Dcard3:
        Dcard3_num = 2
    if '3' in Dcard3:
        Dcard3_num = 3
    if '4' in Dcard3:
        Dcard3_num = 4
    if '5' in Dcard3:
        Dcard3_num = 5
    if '6' in Dcard3:
        Dcard3_num = 6
    if '7' in Dcard3:
        Dcard3_num = 7
    if '8' in Dcard3:
        Dcard3_num = 8
    if '9' in Dcard3:
        Dcard3_num = 9
    if '10' in Dcard3:
        Dcard3_num = 10
    if 'J' in Dcard3:
        Dcard3_num = 10
    if 'Q' in Dcard3:
        Dcard3_num = 10
    if 'K' in Dcard3:
        Dcard3_num = 10

    if '2' in Dcard4:
        Dcard4_num = 2
    if '3' in Dcard4:
        Dcard4_num = 3
    if '4' in Dcard4:
        Dcard4_num = 4
    if '5' in Dcard4:
        Dcard4_num = 5
    if '6' in Dcard4:
        Dcard4_num = 6
    if '7' in Dcard4:
        Dcard4_num = 7
    if '8' in Dcard4:
        Dcard4_num = 8
    if '9' in Dcard4:
        Dcard4_num = 9
    if '10' in Dcard4:
        Dcard4_num = 10
    if 'J' in Dcard4:
        Dcard_num = 10
    if 'Q' in Dcard4:
        Dcard4_num = 10
    if 'K' in Dcard4:
        Dcard4_num = 10

    if '2' in Dcard5:
        Dcard5_num = 2
    if '3' in Dcard5:
        Dcard5_num = 3
    if '4' in Dcard5:
        Dcard5_num = 4
    if '5' in Dcard5:
        Dcard5_num = 5
    if '6' in Dcard5:
        Dcard5_num = 6
    if '7' in Dcard5:
        Dcard5_num = 7
    if '8' in Dcard5:
        Dcard5_num = 8
    if '9' in Dcard5:
        Dcard5_num = 9
    if '10' in Dcard5:
        Dcard5_num = 10
    if 'J' in Dcard5:
        Dcard5_num = 10
    if 'Q' in Dcard5:
        Dcard5_num = 10
    if 'K' in Dcard5:
        Dcard5_num = 10

    print('--------------------------------------------MENU----------------------------------------------------')
    print('1 = Quit')
    print('2 = Rules')
    print('3 = Play')
    direction = input('What do you want to do?')

    if direction == '2':
        print('So your goal is to get the closest number to 21. All numbered cards are worth their writen value, and'
              'face cards are worth 10. Ace is a special case it is worth either 11 or 1 you chose.')

    if direction == '3':
        time.sleep(1)
        print('You were dealt the {0} and the {1}'.format(Pcard1, Pcard2))

        if '2' in Pcard1:
            Pcard1_num = 2
        if '3' in Pcard1:
            Pcard1_num = 3
        if '4' in Pcard1:
            Pcard1_num = 4
        if '5' in Pcard1:
            Pcard1_num = 5
        if '6' in Pcard1:
            Pcard1_num = 6
        if '7' in Pcard1:
            Pcard1_num = 7
        if '8' in Pcard1:
            Pcard1_num = 8
        if '9' in Pcard1:
            Pcard1_num = 9
        if '10' in Pcard1:
            Pcard1_num = 10
        if 'J' in Pcard1:
            Pcard1_num = 10
        if 'Q' in Pcard1:
            Pcard1_num = 10
        if 'K' in Pcard1:
            Pcard1_num = 10
        if 'A' in Pcard1:
            Poo = input('Do you want to make your ace a 1 or 11?')
            Pcard1_num = int(Poo)

        if '2' in Pcard2:
            Pcard2_num = 2
        if '3' in Pcard2:
            Pcard2_num = 3
        if '4' in Pcard2:
            Pcard2_num = 4
        if '5' in Pcard2:
            Pcard2_num = 5
        if '6' in Pcard2:
            Pcard2_num = 6
        if '7' in Pcard2:
            Pcard2_num = 7
        if '8' in Pcard2:
            Pcard2_num = 8
        if '9' in Pcard2:
            Pcard2_num = 9
        if '10' in Pcard2:
            Pcard2_num = 10
        if 'J' in Pcard2:
            Pcard2_num = 10
        if 'Q' in Pcard2:
            Pcard2_num = 10
        if 'K' in Pcard2:
            Pcard2_num = 10
        if 'A' in Pcard2:
            Poo = input('Do you want to make your ace a 1 or 11?')
            Pcard2_num = int(Poo)

        time.sleep(1)
        print('The dealer was dealt the {0} and the {1}'.format(D_censored, Dcard2))
        time.sleep(1)
        Pmove = input('Do want to hit or stand')
        time.sleep(1)

        if Pmove == 'hit':
            if '2' in Pcard3:
                Pcard3_num = 2
            if '3' in Pcard3:
                Pcard3_num = 3
            if '4' in Pcard3:
                Pcard3_num = 4
            if '5' in Pcard3:
                Pcard3_num = 5
            if '6' in Pcard3:
                Pcard3_num = 6
            if '7' in Pcard3:
                Pcard3_num = 7
            if '8' in Pcard3:
                Pcard3_num = 8
            if '9' in Pcard3:
                Pcard3_num = 9
            if '10' in Pcard3:
                Pcard3_num = 10
            if 'J' in Pcard3:
                Pcard3_num = 10
            if 'Q' in Pcard3:
                Pcard3_num = 10
            if 'K' in Pcard3:
                Pcard3_num = 10
            if 'A' in Pcard3:
                Poo = input('Do you want to make your ace a 1 or 11?')
                Pcard3_num = int(Poo)
            Player_end_value = Player_end_value + Pcard4_num

        if Pmove == 'stand':
            print("Okay now it is the dealer's turn, lets see what it does.")
            time.sleep(1)
            Dealers_end_value = Dcard1_num + Dcard2_num

            if Dealers_end_value <= 17:
                print('The dealer chose to hit and got the {0}'.format(Dcard3))
                print('Dealers cards:')
                print(Dcard1)
                print(Dcard2)
                print(Dcard3)
                Dealers_end_value = Dealers_end_value + Dcard3_num
                time.sleep(1)

            if Dealers_end_value >= 17:
                print('The dealer chose to stand')
                time.sleep(1)
                Player_end_value = Player_end_value
                if Dealers_end_value <= 21 and Player_end_value <= 21:
                    if Dealers_end_value > Player_end_value:
                        print('You lost')
                    else:
                        print('You won')
                else:
                    if Dealers_end_value > 21:
                        print('The Dealer busted you win')
                    if Player_end_value > 21:
                        print('You busted and the Dealer won')

                if Dealers_end_value <= 17:
                    print('The dealer chose to hit and got the {0}'.format(Dcard4))
                    print('Dealers cards:')
                    print(Dcard1)
                    print(Dcard2)
                    print(Dcard3)
                    print(Dcard4)
                    Dealers_end_value = Dealers_end_value + Dcard4_num
                    time.sleep(1)

                if Dealers_end_value >= 17:
                    print('The dealer chose to stand')
                    time.sleep(1)
                    if Dealers_end_value <= 21 and Player_end_value <= 21:
                        if Dealers_end_value > Player_end_value:
                            print('You lost')
                        else:
                            print('You won')
                    else:
                        if Dealers_end_value > 21:
                            print('The Dealer busted you win')
                        if Player_end_value > 21:
                            print('You busted and the Dealer won')

                    if Dealers_end_value <= 17:
                        print('The dealer chose to hit and got the {0}'.format(Dcard5))
                        print('Dealers cards:')
                        print(Dcard1)
                        print(Dcard2)
                        print(Dcard3)
                        print(Dcard4)
                        print(Dcard5)
                        Dealers_end_value = Dealers_end_value + Dcard5_num
                        time.sleep(1)
                        print('The dealer chose to stand')
                        time.sleep(1)
                        if Dealers_end_value <= 21 and Player_end_value <= 21:
                            if Dealers_end_value > Player_end_value:
                                print('You lost')
                            else:
                                print('You won')
                        else:
                            if Dealers_end_value > 21:
                                print('The Dealer busted you win')
                            if Player_end_value > 21:
                                print('You busted and the Dealer won')

                    if Dealers_end_value > 17:
                        print('The Dealer chose to stand')
                        time.sleep(1)
                        if Dealers_end_value <= 21 and Player_end_value <= 21:
                            if Dealers_end_value > Player_end_value:
                                print('You lost')
                            else:
                                print('You won')
                        else:
                            if Dealers_end_value > 21:
                                print('The Dealer busted you win')
                            if Player_end_value > 21:
                                print('You busted and the Dealer won')

            time.sleep(1)
            Pmove = input('Do you want to hit or stand?')
            time.sleep(1)
            print('You got the {0}'.format(Pcard4))

            if Pmove == 'hit':
                if '2' in Pcard4:
                    Pcard4_num = 2
                if '3' in Pcard4:
                    Pcard4_num = 3
                if '4' in Pcard4:
                    Pcard4_num = 4
                if '5' in Pcard4:
                    Pcard4_num = 5
                if '6' in Pcard4:
                    Pcard4_num = 6
                if '7' in Pcard4:
                    Pcard4_num = 7
                if '8' in Pcard4:
                    Pcard4_num = 8
                if '9' in Pcard4:
                    Pcard4_num = 9
                if '10' in Pcard4:
                    Pcard4_num = 10
                if 'J' in Pcard4:
                    Pcard4_num = 10
                if 'Q' in Pcard4:
                    Pcard4_num = 10
                if 'K' in Pcard4:
                    Pcard4_num = 10
                if 'A' in Pcard4:
                    Poo = input('Do you want to make your ace a 1 or 11?')
                    Pcard4_num = int(Poo)
                Player_end_value = Player_end_value + Pcard4_num

            if Pmove == 'stand':
                print("Okay now it is the dealer's turn, lets see what it does.")
                time.sleep(1)
                Dealers_end_value = Dcard1_num + Dcard2_num

                if Dealers_end_value <= 17:
                    print('The dealer chose to hit and got the {0}'.format(Dcard3))
                    print('Dealers cards:')
                    print(Dcard1)
                    print(Dcard2)
                    print(Dcard3)
                    Dealers_end_value = Dealers_end_value + Dcard3_num
                    time.sleep(1)

                if Dealers_end_value >= 17:
                    print('The dealer chose to stand')
                    time.sleep(1)
                    Player_end_value = Player_end_value
                    if Dealers_end_value <= 21 and Player_end_value <= 21:
                        if Dealers_end_value > Player_end_value:
                            print('You lost')
                        else:
                            print('You won')
                    else:
                        if Dealers_end_value > 21:
                            print('The Dealer busted you win')
                        if Player_end_value > 21:
                            print('You busted and the Dealer won')

                    if Dealers_end_value <= 17:
                        print('The dealer chose to hit and got the {0}'.format(Dcard4))
                        print('Dealers cards:')
                        print(Dcard1)
                        print(Dcard2)
                        print(Dcard3)
                        print(Dcard4)
                        Dealers_end_value = Dealers_end_value + Dcard4_num
                        time.sleep(1)

                    if Dealers_end_value >= 17:
                        print('The dealer chose to stand')
                        time.sleep(1)
                        if Dealers_end_value <= 21 and Player_end_value <= 21:
                            if Dealers_end_value > Player_end_value:
                                print('You lost')
                            else:
                                print('You won')
                        else:
                            if Dealers_end_value > 21:
                                print('The Dealer busted you win')
                            if Player_end_value > 21:
                                print('You busted and the Dealer won')

                        if Dealers_end_value <= 17:
                            print('The dealer chose to hit and got the {0}'.format(Dcard5))
                            print('Dealers cards:')
                            print(Dcard1)
                            print(Dcard2)
                            print(Dcard3)
                            print(Dcard4)
                            print(Dcard5)
                            Dealers_end_value = Dealers_end_value + Dcard5_num
                            time.sleep(1)
                            print('The dealer chose to stand')
                            time.sleep(1)
                            if Dealers_end_value <= 21 and Player_end_value <= 21:
                                if Dealers_end_value > Player_end_value:
                                    print('You lost')
                                else:
                                    print('You won')
                            else:
                                if Dealers_end_value > 21:
                                    print('The Dealer busted you win')
                                if Player_end_value > 21:
                                    print('You busted and the Dealer won')

                        if Dealers_end_value > 17:
                            print('The Dealer chose to stand')
                            time.sleep(1)
                            if Dealers_end_value <= 21 and Player_end_value <= 21:
                                if Dealers_end_value > Player_end_value:
                                    print('You lost')
                                else:
                                    print('You won')
                            else:
                                if Dealers_end_value > 21:
                                    print('The Dealer busted you win')
                                if Player_end_value > 21:
                                    print('You busted and the Dealer won')

                time.sleep(1)
                Pmove = input('Do you want to hit or stand?')
                time.sleep(1)
                print('You got the {0}'.format(Pcard4))

                if Pmove == 'hit':
                    if '2' in Pcard5:
                        Pcard5_num = 2
                    if '3' in Pcard5:
                        Pcard5_num = 3
                    if '4' in Pcard5:
                        Pcard5_num = 4
                    if '5' in Pcard5:
                        Pcard5_num = 5
                    if '6' in Pcard5:
                        Pcard5_num = 6
                    if '7' in Pcard5:
                        Pcard5_num = 7
                    if '8' in Pcard5:
                        Pcard5_num = 8
                    if '9' in Pcard5:
                        Pcard5_num = 9
                    if '10' in Pcard5:
                        Pcard5_num = 10
                    if 'J' in Pcard5:
                        Pcard5_num = 10
                    if 'Q' in Pcard5:
                        Pcard5_num = 10
                    if 'K' in Pcard5:
                        Pcard5_num = 10
                    if 'A' in Pcard5:
                        Poo = input('Do you want to make your ace a 1 or 11?')
                        Pcard5_num = int(Poo)
                    Player_end_value = Player_end_value + Pcard5_num

                if Pmove == 'stand':
                    print("Okay now it is the dealer's turn, lets see what it does.")
                    time.sleep(1)
                    Dealers_end_value = Dcard1_num + Dcard2_num

                    if Dealers_end_value <= 17:
                        print('The dealer chose to hit and got the {0}'.format(Dcard3))
                        print('Dealers cards:')
                        print(Dcard1)
                        print(Dcard2)
                        print(Dcard3)
                        Dealers_end_value = Dealers_end_value + Dcard3_num
                        time.sleep(1)

                    if Dealers_end_value >= 17:
                        print('The dealer chose to stand')
                        time.sleep(1)
                        Player_end_value = Player_end_value
                        if Dealers_end_value <= 21 and Player_end_value <= 21:
                            if Dealers_end_value > Player_end_value:
                                print('You lost')
                            else:
                                print('You won')
                        else:
                            if Dealers_end_value > 21:
                                print('The Dealer busted you win')
                            if Player_end_value > 21:
                                print('You busted and the Dealer won')

                        if Dealers_end_value <= 17:
                            print('The dealer chose to hit and got the {0}'.format(Dcard4))
                            print('Dealers cards:')
                            print(Dcard1)
                            print(Dcard2)
                            print(Dcard3)
                            print(Dcard4)
                            Dealers_end_value = Dealers_end_value + Dcard4_num
                            time.sleep(1)

                        if Dealers_end_value >= 17:
                            print('The dealer chose to stand')
                            time.sleep(1)
                            if Dealers_end_value <= 21 and Player_end_value <= 21:
                                if Dealers_end_value > Player_end_value:
                                    print('You lost')
                                else:
                                    print('You won')
                            else:
                                if Dealers_end_value > 21:
                                    print('The Dealer busted you win')
                                if Player_end_value > 21:
                                    print('You busted and the Dealer won')

                            if Dealers_end_value <= 17:
                                print('The dealer chose to hit and got the {0}'.format(Dcard5))
                                print('Dealers cards:')
                                print(Dcard1)
                                print(Dcard2)
                                print(Dcard3)
                                print(Dcard4)
                                print(Dcard5)
                                Dealers_end_value = Dealers_end_value + Dcard5_num
                                time.sleep(1)
                                print('The dealer chose to stand')
                                time.sleep(1)
                                if Dealers_end_value <= 21 and Player_end_value <= 21:
                                    if Dealers_end_value > Player_end_value:
                                        print('You lost')
                                    else:
                                        print('You won')
                                else:
                                    if Dealers_end_value > 21:
                                        print('The Dealer busted you win')
                                    if Player_end_value > 21:
                                        print('You busted and the Dealer won')

                            if Dealers_end_value > 17:
                                print('The Dealer chose to stand')
                                time.sleep(1)
                                if Dealers_end_value <= 21 and Player_end_value <= 21:
                                    if Dealers_end_value > Player_end_value:
                                        print('You lost')
                                    else:
                                        print('You won')
                                else:
                                    if Dealers_end_value > 21:
                                        print('The Dealer busted you win')
                                    if Player_end_value > 21:
                                        print('You busted and the Dealer won')


print('Thanks for checking this out.')
