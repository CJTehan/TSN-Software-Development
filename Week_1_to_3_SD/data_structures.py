# Using Python list as an array
grades = [90, 85, 77, 92]
print("First student's grade:", grades[0])

# Using Python's collections.deque as a linked list
from collections import deque
playlist = deque(["Song1", "Song2", "Song3"])
print(playlist[1])

# Using Python list as a stack
stack = []
stack.append("Undo1")
stack.append("Undo2")
last_undo = stack.pop()
print("Last undo:", last_undo)
#print(stack[0])
#print(stack[1])

# Using Python's queue.Queue as a queue
from queue import Queue
q = Queue()
q.put("Print1")
q.put("Print2")
first_print = q.get()
print("First print job:", first_print)

# Using Python's queue.Queue as a queue last
# from queue import LifoQueue
from queue import LifoQueue
q = LifoQueue()
q.put("Print1")
q.put("Print2")
last_print = q.get()
print("Last print job:", last_print)

# Specific
from collections import deque
q = deque(["apple", "banana", "cherry"])
second_item = q[1] # Access the second item (index 1)
print(second_item) # Output: banana

