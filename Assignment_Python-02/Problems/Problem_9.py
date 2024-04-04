'''
Problem 8: Find Duplicate Elements
Write a Python function to find all duplicate elements in a list and return them in a new list.
List = [1, 2, 3, 2, 4, 5, 4, 6]
'''

def remove_duplicates(nums):
    unique_elements = list(set(nums))
    
    for i in range(len(unique_elements)):
        nums[i] = unique_elements[i]
    
    return unique_elements

List = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
new_length = remove_duplicates(List)
print(new_length)  


