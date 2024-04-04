''' 
Problem 4: Count Vowels and Consonants
Write a Python function to count the number of vowels and consonants in a given string "Hello
World"
'''

def count_vowel_consonant(str):
    vowel = 0
    consonant = 0
    

    for item in range(len(str)):
        if str[item] == 'a' or str[item] == 'e' or str[item] == 'i' or str[item] == 'o'  or str[item] == 'u' or str[item] == 'A' or str[item] == 'E' or str[item] == 'I' or str[item] == 'O'  or str[item] == 'U':
            vowel += 1
        elif str[item] == " ":
            continue
        else:
            consonant += 1
            
    return [vowel, consonant]


str='Hello World'
print(count_vowel_consonant(str))