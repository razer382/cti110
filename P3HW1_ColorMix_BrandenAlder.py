#CTI-110
#P3HW1 - Color Mixer
#Branden Aler
#6/23/2020
#

#ask user to enter the two primary colors
color1 = input('Enter the first primary color: ')
color2 = input('Enter the second primary color: ')

if color1 == 'red' and color2 == 'blue':                #if color red and blue are entered
    print('Red and blue make secondary color purple.')  #display the combination of the two
elif color1 == 'blue' and color2 == 'red':              #else if red and blue are entered backwards
    print('Blue and red make secondary color purple.')  #display the combination of the two
    
elif color1 == 'red' and color2 == 'yellow':            #if red and yellow are entered
    print('Red and yellow make the color orange')       #display the combination of the two
elif color1 == 'yellow' and color2 == 'red':            #if yellow and red are entered
    print('yellow and red make the color orange')       #display combination of the two
    
elif color1 == 'blue' and color2 =='yellow':            #if blue and yellow are entered
    print('blue and yellow make green')                 #display combination of the two
elif color1 == 'yellow' and color2 == 'blue':           #if yellow and blue are entered
    print('yellow and blue make green')                 #display combination of the two

    #Displays error message if you don't enter a primary color
elif (color1 != 'yellow' or 'red' or 'blue') or (color2 != 'yellow' or 'red' or 'blue'):
    print('One of the colors you entered is not a primary color') 
