#CTI-110
#P4HW1 - Expenses
#Branden Alder
#6/30/20

#Prompt user to enter amount in account where money will be withdrawn
moneyInAccount = float(input('Enter the amount of money currently in account: '))#Enter amount in account
expense = float(input('Enter the amount of your first expense: '))               #Enter amount of first expense
totalMoney = moneyInAccount - expense                                            #Subtract expense from account
anotherExpense = 'y'                                                             #Declare anotherExpense at value y
totalExpenses = 0                                                                #Declare totalExpenses

while anotherExpense == 'y':                                                 #While anotherExpense equal y
    anotherExpense = input('Would you like to add another expense? (y/n): ') #Asks user if They'd like to put in another expense
    totalExpenses += 1                                                       #Increases expense count per iteration
    if anotherExpense == 'y':                                                #If you want another expense
       expense = float(input('Enter the amount of your other expense: '))    #Ask for new expense value
       totalMoney -= expense                                                 #Decrease new expense from totalMoney
    elif anotherExpense == 'n':                                              #Else if you dont want another expense
        break                                                                #Break from loop                     
    
print('')                                                             #Blank line
print('Amount in account before expenses: ', moneyInAccount)          #Print number in account before expenses
print('Number of expenses entered: ', totalExpenses)                  #Print number of expenses entered
print('Amount in account AFTER expenses subtracted is ', totalMoney)  #Print amount in account after expenses have been taken out
