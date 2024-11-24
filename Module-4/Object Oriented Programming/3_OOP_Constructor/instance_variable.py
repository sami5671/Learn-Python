class MyClass():
    
    x = 10
    y = 20
    # z = 100

    # constructor 
    def __init__(self, zValue, xValue):  
        self.z = zValue 
        self.x = xValue

    # instance method
    def addTow(self):
        print(self.x + self.y + self.z)


# creating object of MyClass and passing z and x values
obj = MyClass(100, 500)

obj.addTow()