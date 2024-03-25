''' Write a function that takes 2 numbers as arguments (age of two brothers)
 and find who is elder'''

# Function  for comparing two brother age
def compareAge(param_1, param_2):
    if param_1 > param_2:
        print('1st brother is elder than 2nd brother')
    else:
        print('2nd brother is elder than 1st brother')


# calling the compareAge function

brother_1= input('Enter the 1st brother age: ')
brother_2= input('Enter the 2nd brother age: ')

compareAge(brother_1,brother_2)

