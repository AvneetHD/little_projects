import random
import time

password = input('Put your password so we can crack it')
used_passwords = []
Continue = "False"

Stime = time.time()

while Continue == 'False':
    s = 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', \
        'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'A', 'B', 'C', 'D', 'E', 'F', 'G', \
        'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '!', '@', '#', \
        '$', '%', '^', '&', '*', '(', ')', ',', '?'
    password_len = len(password)


    def password_cracker(password_to_be_cracked, Pass, old_passwords, charecters):
        cracked_password = ""

        CP1 = random.choice(charecters)
        CP2 = random.choice(charecters)
        CP3 = random.choice(charecters)
        CP4 = random.choice(charecters)
        CP5 = random.choice(charecters)
        CP6 = random.choice(charecters)
        CP7 = random.choice(charecters)
        CP8 = random.choice(charecters)
        CP9 = random.choice(charecters)
        CP10 = random.choice(charecters)
        CP11 = random.choice(charecters)
        CP12 = random.choice(charecters)
        CP13 = random.choice(charecters)
        CP14 = random.choice(charecters)
        CP15 = random.choice(charecters)
        CP16 = random.choice(charecters)
        CP17 = random.choice(charecters)
        CP18 = random.choice(charecters)
        CP19 = random.choice(charecters)
        CP20 = random.choice(charecters)
        CP21 = random.choice(charecters)
        CP22 = random.choice(charecters)
        CP23 = random.choice(charecters)
        CP24 = random.choice(charecters)
        CP25 = random.choice(charecters)
        CP26 = random.choice(charecters)
        CP27 = random.choice(charecters)
        CP28 = random.choice(charecters)
        CP29 = random.choice(charecters)
        CP30 = random.choice(charecters)
        CP31 = random.choice(charecters)
        CP32 = random.choice(charecters)

        CP1_CP10 = CP1 + CP2 + CP3 + CP4 + CP5 + CP6 + CP7 + CP8 + CP9 + CP10
        CP10_CP20 = CP1_CP10 + CP11 + CP12 + CP13 + CP14 + CP15 + CP16 + CP17 + CP18 + CP19 + CP20
        CP20_30 = CP10_CP20 + CP21 + CP22 + CP23 + CP24 + CP25 + CP26 + CP27 + CP28 + CP29 + CP30

        if password_len == 1:
            cracked_password = CP1
        if password_len == 2:
            cracked_password = CP1 + CP2
        if password_len == 3:
            cracked_password = CP1 + CP2 + CP3
        if password_len == 4:
            cracked_password = CP1 + CP2 + CP3 + CP4
        if password_len == 5:
            cracked_password = CP1 + CP2 + CP3 + CP4 + CP5
        if password_len == 6:
            cracked_password = CP1 + CP2 + CP3 + CP4 + CP5 + CP6
        if password_len == 7:
            cracked_password = CP1 + CP2 + CP3 + CP4 + CP5 + CP6 + CP7
        if password_len == 8:
            cracked_password = CP1 + CP2 + CP3 + CP4 + CP5 + CP6 + CP7 + CP8
        if password_len == 9:
            cracked_password = CP1 + CP2 + CP3 + CP4 + CP5 + CP6 + CP7 + CP8 + CP9
        if password_len == 10:
            cracked_password = CP1_CP10
        if password_len == 11:
            cracked_password = CP1_CP10 + CP11
        if password_len == 12:
            cracked_password = CP1_CP10 + CP11 + CP12
        if password_len == 13:
            cracked_password = CP1_CP10 + CP11 + CP12 + CP13
        if password_len == 14:
            cracked_password = CP1_CP10 + CP11 + CP12 + CP13 + CP14
        if password_len == 15:
            cracked_password = CP1_CP10 + CP11 + CP12 + CP13 + CP14 + CP15
        if password_len == 16:
            cracked_password = CP1_CP10 + CP11 + CP12 + CP13 + CP14 + CP15 + CP16
        if password_len == 17:
            cracked_password = CP1_CP10 + CP11 + CP12 + CP13 + CP14 + CP15 + CP16 + CP17
        if password_len == 18:
            cracked_password = CP1_CP10 + CP11 + CP12 + CP13 + CP14 + CP15 + CP16 + CP17 + CP18
        if password_len == 19:
            cracked_password = CP1_CP10 + CP11 + CP12 + CP13 + CP14 + CP15 + CP16 + CP17 + CP18 + CP19
        if password_len == 20:
            cracked_password = CP10_CP20
        if password_len == 21:
            cracked_password = CP10_CP20 + CP21
        if password_len == 22:
            cracked_password = CP10_CP20 + CP21 + CP22
        if password_len == 24:
            cracked_password = CP10_CP20 + CP21 + CP22 + CP23 + CP24
        if password_len == 25:
            cracked_password = CP10_CP20 + CP21 + CP22 + CP23 + CP24 + CP25
        if password_len == 26:
            cracked_password = CP10_CP20 + CP21 + CP22 + CP23 + CP24 + CP25 + CP26
        if password_len == 27:
            cracked_password = CP10_CP20 + CP21 + CP22 + CP23 + CP24 + CP25 + CP26 + CP27
        if password_len == 28:
            cracked_password = CP10_CP20 + CP21 + CP22 + CP23 + CP24 + CP25 + CP26 + CP27 + CP28
        if password_len == 29:
            cracked_password = CP10_CP20 + CP21 + CP22 + CP23 + CP24 + CP25 + CP26 + CP27 + CP28 + CP29
        if password_len == 30:
            cracked_password = CP20_30
        if password_len == 31:
            cracked_password = CP20_30 + CP31
        if password_len == 32:
            cracked_password = CP20_30 + CP31 + CP32
        old_passwords.append(cracked_password)

        if cracked_password == password:
            Pass = 'True'

        else:
            Pass = 'False'

Ftime = time.time()
Etime = Ftime - Stime
print('we have cracked your password using %i passwords' % len(used_passwords))
time.sleep(1)
print(used_passwords)
print(Etime)
