import random
result = ""
message = ""
choice = ""
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

while choice != '0':
    number = random.choice(numbers)
    choice = input('Do you want to encrypt or decrypt\nEnter 1 to encrypt, 2 to decrypt, and 0 to exit.')

    if choice == '1':
        message = input('Enter Message for Encryption.')
        for i in range(0, len(message)):
            result = result + chr(ord(message[i])-2)

        print(result)
        result = ''

    elif choice == '2':
        message = input('Enter Message for Decryption.')
        for i in range(0, len(message)):
            result = result + chr(ord(message[i])+2)

        print(result)
        result = ''
