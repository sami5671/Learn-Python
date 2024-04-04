''' Problem 6: Count Occurrences
 Write a Python function to count the occurrences of each element in a list and return a dictionary
 with the counts.
 List = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]'''

def find_occurrence(list):
    counts = {}
    for item in list:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1
    return counts


list = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
result = find_occurrence(list)
print(result)
