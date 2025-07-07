class MyClass():

    x = 10
    y = 20

    @staticmethod
    def addTow():
         z = MyClass.x + MyClass.y
         print(z)


#access variables directly from class
print(MyClass.x)
print(MyClass.x)

# static methods directly
MyClass.addTow()
