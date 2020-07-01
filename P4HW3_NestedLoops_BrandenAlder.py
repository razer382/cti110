#Nested loop project
#7/1/2020
#CTI-110 P4HW3 - Nested Loops
#Branden Alder
#

for row in range(6):            #For loops for the 6 rows
    print('#', end = '')        #Print the # 
    for spaces in range( row ): #For loop for spaces tied to row iterations starting from 0
        print(' ', end = '')    #Print space
    print('#')                  #Print # at the end of each row
    
