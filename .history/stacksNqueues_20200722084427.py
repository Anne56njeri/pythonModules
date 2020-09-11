# we'll use a list to rep stack and a queue
#  empty list 
# stack is last in first out 
stack = []
stack.append(1) 
stack.append(2) 
stack.append(3) 
stack.append(4)

# remove item from stack(pop)
x = stack.pop()

from collections import deque
# create empty deque 
queue = deque()

queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)
print(queue)
# remove elements from the front of the list 
y = queue.popleft
