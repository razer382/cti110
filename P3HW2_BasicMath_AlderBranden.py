#CTI-110
#P3HW2 - Basic Math
#Branden Alder
#6/23/2020
#

num1 = float(input('Enter a number: '))        #Ask user to enter first number
num2 = float(input('Enter a second number: ')) #Ask user to enter second number

print('--------------MENU----------')          #Menu stuffs
print('1) Add Numbers')
print('2) Multiply Numbers')
print('3) Subtract Nubmers')
print('4) Exit')
print('----------------------------')
choice = input('Pick an option from the menu: ') #User input for choice from menu
if choice == '1':                                #If choice 1 is selected
    print('The sum is: ', num1 + num2)           #Sum of two numbers
elif choice == '2':                              #If choice 2 is selected
    print('The numbers multiplied: ', num1 * num2)#Two numbers multiplied
elif choice == '3':                              #If choice 3 is selected
    print('The numbers subtracted: ', num1 - num2)#Subtract the numbers
elif choice == '4':                              #If choice 4 is selected
    print('The program will now terminate')      #Message to terminate program
elif choice != '1' or '2' or '3' or '4':         #If choice isnt in the Menu
    print('Incorrect choice entered.')           #Display incorrect choice
