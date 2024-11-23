class A:
    def __init__(self):
        print("Creating Object for class A")
    
    def jump(self):
        print("I am jumping")

class AA(A):
    def __init__(self):
        print("Creating Object for class AA")
    
    def jump(self):  # method overriding
        print("yes, I am jumping!!!!!!!!!")

a = A()
b = A()
c = AA()

a.jump()
c.jump()