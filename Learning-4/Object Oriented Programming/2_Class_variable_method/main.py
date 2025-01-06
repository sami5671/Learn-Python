
# create class
class MyClass:
    x=10 # class variable
    y=30
    z=40
    sum = x+y+z

    def addTow(self, a, b): # class method
        sum = self.x+self.y+self.z+ a + b
        print("Sum: ", sum)
    
    def addNew(self):
        self.addTow(10,10)

obj = MyClass()

obj.addTow(5, 5)
obj.addNew()
