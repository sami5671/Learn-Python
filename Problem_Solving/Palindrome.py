

def Check_palindrome(words):

    palindrome_count = 0;

    for item in words:
     if item.lower() == item.lower()[::-1]:
       palindrome_count = palindrome_count + 1;
    
    return palindrome_count;
 



words=["raDaR", 'level', 'noon', 'deifieD']

palindrome_count=Check_palindrome(words)

print(palindrome_count)


