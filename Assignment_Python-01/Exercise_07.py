'''Write a function that takes 1 number as argument. The function should return “Fizz” if
 the number is divisible by 3, the function should return “Buzz” if the number is divisible
 by 5, the function should return “FizzBuzz” if the number is divisible by both 5 and 3,
 otherwise return “Not a Fizz-buzz number”'''

# check fizz-buzz
def check_FizzBuzz(param):
    if (param % 3 == 0) and (param % 5 == 0):
        print("FizzBuzz")
    elif (param % 5 == 0):
        print('Buzz')
    elif (param % 3 == 0):
        print('Fizz')
    else:
        print('Not a Fizz-buzz number')

# calling the function
      
number=int(input('Enter a number to check FizzBuzz: '))
check_FizzBuzz(number)