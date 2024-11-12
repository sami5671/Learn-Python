
# using the + operator
string1 = "Hello"
string2 = "World"

concat = string1 + ", " +  string2

print(concat)

# using the join() method
string1 = "Hello"
string2 = "World"

concat = ", ".join([string1, string2])

print(concat)


# using formatted string literals (f-strings)
string1 = "Hello"
string2 = "World"

concat = f"{string1}, {string2} "

print(concat)


# using format() method
string1 = "Hello"
string2 = "World"
combined = "{}, {}!".format(string1, string2)
print(combined) # Output: Hello, World!

# using % formatting
string1 = "Hello"
string2 = "World"
combined = "%s, %s!" % (string1, string2)
print(combined) # Output: Hello, World!
