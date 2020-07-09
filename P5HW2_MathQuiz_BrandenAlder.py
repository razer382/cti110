#Math Quiz Project
#7/9/2020
#CTI-110 P5HW2 - Math Quiz
#Branden Alder
#

#Write a program that gives simple math quizzes. The program should display
#two random numbers that are to be added. The program should allow the student
#to answer. If incorrect, a message showing correct answer should be displayed
#
import random       #Import random

def createRandomNums(): #function to create random numbers
    num1 = random.randint(1, 5)
    return num1

def askUserNumber(message = 'Add the numbers: '): #function to ask the user to add the numbers
    userNumber = int(input(message))
    return userNumber

def askUserNumber2(message = 'Subtract the numbers: '): #function to ask the user subtract numbers 
    userNumber = int(input(message))
    return userNumber

def checkUserNumber(num1, num2, userNumber): #function to check if user is correct in addition
    addNum = num1 + num2
    if addNum != userNumber:
        return 'Incorrect. The correct answer is: ', num1 + num2
    if addNum == userNumber:
        return 'Congratulations!'
    
def checkUserNumber2(num1, num2, userNumber): #function to check if user is correct in subtraction
    subNum = num1 - num2
    if subNum != userNumber:
        return 'Incorrect. The correct answer is: ', num1 - num2
    if subNum == userNumber:
        return 'Congratulations!'

def main():
    num1 = createRandomNums() #get first random number
    num2 = createRandomNums() #get second random number
    
    print('Main Menu')       #menu stuffs
    print('----------------')
    print('1)Add Random Numbers')
    print('2)Subtract Random Numbers')
    print('3)Exit')
    choice = input('Pick an option from the menu: ')
    
    while choice != '3': #while choice doesnt equal exit value
        if choice == '1':#if user enters 1 it asks user to add the numbers 
                 print('Add these two numbers: ', num1,',', num2)
                 userNumber = askUserNumber()   #go to function to ask user number
                 message = checkUserNumber(num1, num2, userNumber) #function to subtract numbers 
                 if message == ('Congratulations!'):#if correct
                     print(message)
                     main() #restart menu and choice
                 if message == ('Incorrect. The correct answer is: ', num1 + num2): #if wrong
                     print('Incorrect the correct answer is:',num1 +num2)
                     main() #restart menu and choice
        if choice == '2': #if choice is to subtract
            print('Subtract these two numbers: ', num1,',', num2) 
            userNumber = askUserNumber2() #ask user to subtract
            message2 = checkUserNumber2(num1, num2, userNumber) #function to subtract and see if correct or not
            if message2 == ('Congratulations!'): #if right
                print(message2)
                main() #go back to main
            if message2 == ('Incorrect. The correct answer is: ',num1 - num2): #if incorrect 
                print('Incorrect, the correct answer is:',num1-num2) 
                main()#go back to menu
    if choice == '3': #exit 
        exit()
                    
                     
                 
main() #call main
