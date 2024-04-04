'''
Problem 8: Find Duplicate Elements
Write a Python function to find all duplicate elements in a list and return them in a new list.
List = [1, 2, 3, 2, 4, 5, 4, 6]
 '''

def find_duplicates(nums):
    new_list = []
    duplicates = set()

    for item in nums:
        if item in duplicates:
            new_list.append(item)
        else:
            duplicates.add(item)

    return new_list


List = [1, 2, 3, 2, 4, 5, 4, 6]
result = find_duplicates(List)
print(result)
