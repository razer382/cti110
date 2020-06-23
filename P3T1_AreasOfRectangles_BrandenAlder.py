#Areas Of Rectangles
#6/23/2020
#CTI-110 P3T1 - Areas of Rectangles
#Branden Alder

#Input length and width rect 1
length1 = int(input('Enter the length of rectangle 1: '))
width1 = int(input('Enter the width of rectangle 1: '))
#input the length and width of rectangle 2.
length2 = int(input('Enter the length of rectangle 2: '))
width2 = int(input('Enter the width of rectangle 2: '))
#calculate the area of rectangle 1
area1 = length1 * width1
#calculate the area of rectangle 2
area2 = length2 * width2
#if area1 > area2 display rectangle 1 is greater
if area1 > area2:
    print('Rectangle 1 has the greater area.')
#else if area2 > area1 display rectangle 2 is greater
elif area2 > area1:
    print('Rectangle 2 has the greater area.')
#else (they're the same)
else:
    print('Both have the same area.')
