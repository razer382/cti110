#Random Number Project
#7/7/2020
#CTI-110 P5HW1 - Random Number
#Branden Alder
#

 
import random #import random so you can get random numbers 

def createRandomNumber(): #create random number function
    randomNumber = random.randint(1,100) #create a random number between 1-100
    return randomNumber 

def askUserNumber(message = 'Guess the Number: '): #Create function to ask user their number
    userNumber = int(input(message))
    return userNumber

def checkUserNumber( userNumber, randomNumber ): #Function to check if users number is too high, too low, or accurate
    if userNumber > randomNumber:
        return 'Your guess is too high'
    elif userNumber < randomNumber:
        return 'Your guess is too low'
    else:
        return 'Congratulations, you guessed correctly!'

def main(): #Main function that pulls other functions and brings it all together
    userCongratulated = False
    start = True
    print('MAIN MENU')      #menu stuffs
    print('---------------')
    print('1) Play Game')
    print('2) Exit Game')
    choice = input('Pick an option from the menu: ')
    if choice == '1':           #if choice is 1 it will start the game
        while userCongratulated or start:
            numberOfGuesses = 0 # declare accumulator on number of guesses
            randomNumber = createRandomNumber() 
            # print(randomNumber) #Added this to test the program
            userNumber = askUserNumber()
            numberOfGuesses = numberOfGuesses + 1
            message = checkUserNumber(userNumber, randomNumber)
    
            while message != 'Congratulations, you guessed correctly!': #While you havent guessed right:
                print(message)
                userNumber = askUserNumber('Try again: ')
                numberOfGuesses = numberOfGuesses + 1 #increases count of tries
                message = checkUserNumber( userNumber, randomNumber)
            print(message)
            print(' It took you', numberOfGuesses, 'tries')
            userCongratulated = True
            main() #call main function/menu after you've guessed correctly
    if choice == '2':
        exit()


main()
