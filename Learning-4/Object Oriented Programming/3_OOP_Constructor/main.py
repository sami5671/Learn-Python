class MyClass():
    
    x = 10
    y = 20
    def __init__(self, a , b):  # constructor 
        print("Hello, i am a constructor")
        sum = self.x + self.y + a + b
        print("Sum: ", sum)


obj = MyClass(10, 10)