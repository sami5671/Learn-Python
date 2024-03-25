''' Write a function that takes a number 1 to 9 from the user input (use input function inside
 a function). Store a number in a variable (let’s assume 6). If the input value is less than
 the variable, print (your guess is almost there), if the input value is greater than the
 variable, print- your guess is higher, if the input value and variable are equals, print
Your Guess Is Correct!'''

# function for guessing the number
def guessing_Number():
    number=6
    while(True):
        given_number=int(input('Enter a number: '))

        if given_number >=1 and given_number <=9:

            if number == given_number:
                print('Your Guess Is Correct')
            elif number < given_number:
                print('your guess is higher')
            elif number > given_number:
                print('your guess is almost there')
        else:
            break

# main function

guessing_Number()

