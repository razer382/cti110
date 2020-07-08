#Random Number Project
#7/7/2020
#CTI-110 P5HW1 - Random Number
#Branden Alder
#


import random

def createRandomNumber():
    randomNumber = random.randint(1,100)
    return randomNumber

def askUserNumber(message = 'Guess the Number: '):
    userNumber = int(input(message))
    return userNumber

def checkUserNumber( userNumber, randomNumber ):
    if userNumber > randomNumber:
        return 'Your guess is too high'
    elif userNumber < randomNumber:
        return 'Your guess is too low'
    else:
        return 'Congratulations, you guessed correctly!'

def main():
    userCongratulated = False
    start = True
    print('MAIN MENU')
    print('---------------')
    print('1) Play Game')
    print('2) Exit Game')
    choice = input('Pick an option from the menu: ')
    if choice == '1':
        while userCongratulated or start:
            numberOfGuesses = 0
            randomNumber = createRandomNumber()
            print(randomNumber)
            userNumber = askUserNumber()
            numberOfGuesses = numberOfGuesses + 1
            message = checkUserNumber(userNumber, randomNumber)
    
            while message != 'Congratulations, you guessed correctly!':
                print(message)
                userNumber = askUserNumber('Try again: ')
                numberOfGuesses = numberOfGuesses + 1
                message = checkUserNumber( userNumber, randomNumber)
            print(message)
            print(' It took you', numberOfGuesses, 'tries')
            userCongratulated = True
            main()
    if choice == '2':
        exit()


main()
