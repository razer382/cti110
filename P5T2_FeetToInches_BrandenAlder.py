#Feet to inches Project
#7/7/2020
#CTI-110 P5T2_FeetToInches
#Branden Alder
#

INCHES_PER_FOOT = 12 #Define constant inches per foot

def main(): #Define main function
    feet = int(input('Enter a number of feet: ')) #User inputs feet

    print(feet, 'equals', feet_to_inches(feet), 'inches.') #Convert feet to inches

# The feet_to_inches function converts feet to inches.
def feet_to_inches(feet): #define feet to inches
    return feet * INCHES_PER_FOOT

#Call main function.
main()
