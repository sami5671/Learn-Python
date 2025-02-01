import csv 

with open("data.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age", "City"])
    writer.writerow(["John", 30, "New York"])
    writer.writerow(["Jane", 25, "Los Angeles"])
    writer.writerow(["Bob", 28, "Chicago"])
    
    