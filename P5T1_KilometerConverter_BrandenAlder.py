#Kilometer Converter Project
#7/7/2020
#CTI-110 P5T1_KilometerConverter
#Branden Alder
#

CONVERSION_FACTOR = 0.6214 #Define constant value

def main():                #Main function gets a distance in kilometers and calls
    kilometers = float(input('Enter a distance in kilometers: ')) #Get the Distance in kilometers.

    show_miles(kilometers) #Display distance converted to miles.

def show_miles(km):                #Define Function
    miles = km * CONVERSION_FACTOR #Calculates miles

    print(km, 'kilometers equals', miles, 'miles') #Display miles

main() #calls the main function 
