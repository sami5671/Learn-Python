"""- How child can access parents static and non-static properties
"""

class Father:

    x = 10
    y = 20

    def addTwoFather(self):
        return self.x + self.y
    
class Son(Father):
    
    def addTwoSon(self):
        sum = self.addTwoFather() + 100
        print(sum)

obj = Son()
obj.addTwoSon()
