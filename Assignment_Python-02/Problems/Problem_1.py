''' 
Problem 1: Fibonacci Sequence
Write a Python function to generate the Fibonacci sequence up to a specified number n. Where
n=100
'''

def Fibonacci_sequence(n):
    first = 0
    second = 1

    print(first)
    print(second)
    
    while True:
      next_value = first + second
      if next_value <= n:
        print(next_value)
        first = second
        second = next_value
      else:
         break


number = 100
Fibonacci_sequence(number)

