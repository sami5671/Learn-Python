class Stack:

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return "Stack is empty"

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return "Stack is empty"
# Edge case
    def is_empty(self):
        return len(self.items) == 0
    

my_stack = Stack()

# Push some items onto the stack
my_stack.push(5)
my_stack.push(10)
my_stack.push(15)

# [5, 10, 15]

# Peek at the top item of the stack
print("Top item of the stack:", my_stack.peek())  

# Pop an item from the stack
popped_item = my_stack.pop()
print("Popped item:", popped_item)  

# Peek at the top item of the stack again
print("Top item of the stack:", my_stack.peek())  

# Pop another item from the stack
popped_item = my_stack.pop()
print("Popped item:", popped_item)  

# Check if the stack is empty
print("Is the stack empty?", my_stack.is_empty())  

# Pop the remaining item from the stack
popped_item = my_stack.pop()
print("Popped item:", popped_item)  

# Check if the stack is empty again
print("Is the stack empty?", my_stack.is_empty())  

# Try to pop from an empty stack
popped_item = my_stack.pop()
print("Popped item:", popped_item)  

# Try to peek into an empty stack
print("Top item of the stack:", my_stack.peek())  