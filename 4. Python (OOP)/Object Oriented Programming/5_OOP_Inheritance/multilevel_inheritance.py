# Multilevel Inheritance Example
class GrandFather: 
    x = 10
    y = 20

    def add(self):
        print(self.x + self.y)
    
    def sub(self):
        print(self.x - self.y)


class Father(GrandFather):
    pass

class Son(Father):
    pass

# creating object of child class
obj = Son()

# accessing methods and attributes of parent class
obj.add()  # Output: 30
obj.sub()  # Output: -10

