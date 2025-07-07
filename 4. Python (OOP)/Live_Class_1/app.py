import time

class Car:

    year = 2024
    def __init__(self, a,b,c="White"): # constructor (__init__ ---> Magic method)
        self.make = a
        self.model = b
        self.color = c
    
    def __str__(self):
        return f"Car detail: {self.make}---{self.model}---{self.color}"
    
    def start_engine(self, t=2):
        self.year = 1900
        print("Starting the engine....")
        time.sleep(t)
        print("Engine started! Ready to Go!")


# making object of car

car1 = Car("Subaru", "Forester", "Bronze")
car2 = Car("Toyota", "Parado", "Bronze")
car3 = Car("Subaru", "Forester")

# calling methods
print("Before starting the engine", car1.year)
car1.start_engine()
print("After start the Engine", car1.year)


