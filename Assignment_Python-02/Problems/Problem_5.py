''' 
Problem 5: Palindrome Check
Write a Python function to check if a given string is a palindrome or not.
String = "A man, a plan, a canal, Panama"
'''

def check_palindrome(str):

    given_string = str
    reversed_string = given_string[::-1]
    
    if given_string == reversed_string:
       return True
    else:
       return False


str = "A man, a plan, a canal, Panama"

if check_palindrome(str):
  print("The string is a palindrome")
else:
   print("The string is not a palindrome")
