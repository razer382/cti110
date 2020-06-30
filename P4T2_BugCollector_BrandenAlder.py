#Bug Collector Project
#6/30/2020
#CTI-110 P4T2 - Bug Collector
#Branden Alder
#

total = 0  #Initialize accumulator.

for day in range(1, 8): #For loop declaring starting number and the number the loop ends on
    print('Enter the bugs collected on day', day, ':') #Prompt user for bugs collected
    bugs =int(input()) #Input the number of bugs
    total += bugs #Adds bugs to accumulator

#Display the total bugs
print('You collected a total of', total, 'bugs.')
