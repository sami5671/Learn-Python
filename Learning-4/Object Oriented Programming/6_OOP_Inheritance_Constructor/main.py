"""
1. When the Parent Class Has a Constructor, but the Child Class Does Not
2. When the Child Class Has a Constructor, but the Parent Class Does Not
3. When Both Parent and Child Classes Have Constructors
4. Accessing the Parent's Constructor
"""


# 1. When the Parent Class Has a Constructor, but the Child Class Does Not
class Father: 
    
    x = 10
    y = 20

    def __init__(self):
        print("Father constructor")

    def add(self): 
        print(self.x + self.y)

# child class 
class Son(Father):
    pass


# creating object 
onj = Son()

# 2. When the Child Class Has a Constructor, but the Parent Class Does Not
class Father: 
    
    x = 10
    y = 20

    def add(self): 
        print(self.x + self.y)

# child class 
class Son(Father):
    
    def __init__(self):
        print("Son constructor")


# creating object 
obj = Son()
obj = Father()

# 3. When Both Parent and Child Classes Have Constructors
class Father: 
    
    x = 10
    y = 20

    def __init__(self):
        print("Father constructor")
    def add(self): 
        print(self.x + self.y)

# child class 
class Son(Father):
    
    def __init__(self):
        print("Son constructor")


# creating object 
obj = Son()

# 4. Accessing the Parent's Constructor
class Father: 
    
    x = 10
    y = 20

    def __init__(self):
        print("Father constructor")
    def add(self): 
        print(self.x + self.y)

# child class 
class Son(Father):
    
    def __init__(self):
        super().__init__()  # accessing parent's constructor
        print("Son constructor")


# creating object 
obj = Son()

