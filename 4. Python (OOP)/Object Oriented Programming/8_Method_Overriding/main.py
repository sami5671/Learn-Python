class Father:

    x = 10
    y = 20
    def add(self):
        print(self.x + self.y)

class Son(Father):
        
    # override method
    def add(self):
        print(self.x + self.y + 100)


obj = Son()
obj.add()