numbers = input()
# slipt numbers into a list

numbers_list = numbers.split(" ")

num1 = int(numbers_list[0])
num2 = int(numbers_list[1])
num3 = int(numbers_list[2])

average = (num1 + num2 + num3) / 3
print(f"Average:{average: .2f}")
