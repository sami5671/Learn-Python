import calculator
from calculator import add, subtract, multiply, divide


# if full module is imported
print(calculator.add(2,4))
print(calculator.subtract(2,4))
print(calculator.multiply(2,4))
print(calculator.divide(2,4))

# if only specific functions are imported
print(add(2,4))
print(subtract(2,4))
print(multiply(2,4))
print(divide(2,4))

