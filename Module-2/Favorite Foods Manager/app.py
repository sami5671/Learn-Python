
favorite_foods = [] # initialize favorite food list

while True:
    print("----------Favorite Foods Manager-------------")
    print("0. Exit")
    print("1. Add foods")
    print("2. Remove foods")
    print("3. View favorite all foods")

    choice = input("Enter your choice: ") # From taken user input 
    
    if choice == "0":
        print("Thanks for using Favorite Foods Manager Application") 
        break
    
    elif choice == "1":
        food = input("Enter a new food: ")
        favorite_foods.append(food) # Add new food to the list
        print(f"{food} added successfully!")
    
    elif choice == "2":
        food = input("Enter the food to remove: ")
        if food in favorite_foods:
            favorite_foods.remove(food)
            print(f"{food} removed successfully!")
        else:
            print("Food not found in the list!")

    elif choice == "3":
        print("Favorite Foods:")
        for food in favorite_foods:
            print(food)


    



