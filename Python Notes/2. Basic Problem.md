
## 1. Fibonacci Series
Write a Python function to generate the Fibonacci sequence up to a specified number n. Where n=100

### Algorithm Steps

1.  It will start with predefined two Variables like a = 0 and b = 1
2. Then there will be a nextValue = a + b
3. Then change the the value of a = b and b = nextValue
4. After that print the nextValue 
5. Then it will continue the process until the process is finished


```python
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
```


##  2. Reverse Words in a String

Write a Python function to reverse the order of words in a given string- "Hello World"

### Algorithm

1. Take input the String and pass to a function
2. Use string reverse method [::-1]
3. Return the reversed string value

```Python
  
def reverse_string(s):

    previous_string = s

    reversed_str = s[::-1]

    print(reversed_str)

  
  

# calling reverse_string function

str = "Hello World"

reverse_string(str)
```
