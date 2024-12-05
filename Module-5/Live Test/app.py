def fibonacci_series_by_terms():
    terms = int(input("Enter the number of terms: "))
    first_value = 0
    second_value = 1
    # fibonacci series
    print( f"Fibonacci Series {terms} terms: ")
   
    for i in range (terms):
        print(first_value, end=" ")
        next_value = first_value + second_value
        first_value =  second_value
        second_value = next_value
        

def fibonacci_series_by_maximumValue():
    first_value = 0
    second_value = 1
    maximum_value = int(input("Enter the maximum value: "))
    # fibonacci series
    print(f"Fibonacci Series up to {maximum_value}: ")
    for i in range (maximum_value):
        if first_value <= maximum_value:
            print(first_value, end= " ")
            next_value = first_value + second_value
            first_value = second_value
            second_value = next_value


while True:
    print("\n=========Choose an option: ")
    print("1. Generate Fibonacci series by terms")
    print("2. Generate Fibonacci series by maximum value")
    print("3. Exit")
    
    choice = input("Enter your choice (1-3): ")
    
    if choice == "1":
        fibonacci_series_by_terms()
    elif choice == "2":
        fibonacci_series_by_maximumValue()
    elif choice == "3":
        break
    else:
        print("Invalid choice. Please select option (1/2/3)")