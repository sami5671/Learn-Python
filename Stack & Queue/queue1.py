class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return "Queue is empty"

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            return "Queue is empty"

    def is_empty(self):
        return len(self.items) == 0

# Create an instance of the Queue class
my_queue = Queue()

# Enqueue some items into the queue
my_queue.enqueue(1)
my_queue.enqueue(2)
my_queue.enqueue(3)


# Peek at the front item of the queue
print("Front item of the queue:", my_queue.peek())  # Output: 1

# Dequeue an item from the queue
dequeued_item = my_queue.dequeue()
print("Dequeued item:", dequeued_item)  

# # Peek at the front item of the queue again
# print("Front item of the queue:", my_queue.peek())  

# # Dequeue another item from the queue
# dequeued_item = my_queue.dequeue()
# print("Dequeued item:", dequeued_item)  

# # Check if the queue is empty
# print("Is the queue empty?", my_queue.is_empty())  

# # Dequeue the remaining item from the queue
# dequeued_item = my_queue.dequeue()
# print("Dequeued item:", dequeued_item)  

# # Check if the queue is empty again
# print("Is the queue empty?", my_queue.is_empty())  

# # Try to dequeue from an empty queue
# dequeued_item = my_queue.dequeue()
# print("Dequeued item:", dequeued_item)  

# # Try to peek into an empty queue
# print("Front item of the queue:", my_queue.peek())  