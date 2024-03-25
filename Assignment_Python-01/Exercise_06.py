''' Write a function named “isLandscape” that takes 2 numbers (image width
 and height) as arguments and the function returns Landscape if the image width has a
 higher value than height. Returns Portrait otherwise'''

# function for comparing
def isLandscape(width, height):
    if (width > height):
      print('Landscape')
    else:
      print('Portrait')
    
# calling function

width=input('Enter the image width: ')
height=input('Enter the image height: ')

isLandscape(width, height)