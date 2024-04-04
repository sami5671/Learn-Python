'''
 Problem 3: Find the Missing Number
 Given a list of n-1 integers from 1 to n, find the missing number in the list.
 List = [1, 2, 4, 6, 3, 7, 8] # Output: 5
'''

def get_sum(nums):
    sum = 0
    for item in nums:
        sum = sum + item
    return sum

def find_missing_num(nums):
    
    n = len(nums) + 1
    total_sum = (n * (n + 1)) / 2
    sum_of_list = get_sum(nums)
    result = total_sum - sum_of_list
    return result


list_numbers =  [1, 2, 4, 6, 3, 7, 8]
missing_number = find_missing_num(list_numbers)
print(int(missing_number))


