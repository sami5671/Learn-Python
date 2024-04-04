''' Problem 7: Merge Sorted Lists
 Write a Python function to merge two sorted lists into a single sorted list.
 List1 = [1, 3, 5]
 List2 = [2, 4, 6]
 '''

def merged_sorted_list(list_1, list_2):

    result = sorted(list_1+ list_2)
    return result
     

list_1 = [1,3,5]
list_2 = [2,4,6]

result = merged_sorted_list(list_1, list_2)
print(result)