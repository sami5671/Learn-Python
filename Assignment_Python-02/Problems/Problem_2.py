'''
Problem 2: Reverse Words in a String
Write a Python function to reverse the order of words in a given string- "Hello World"
'''

def reverse_string(s):
    
    previous_string = s
    reversed_str = s[::-1]
    print(reversed_str)


# calling reverse_string function
str = "Hello World"
reverse_string(str)