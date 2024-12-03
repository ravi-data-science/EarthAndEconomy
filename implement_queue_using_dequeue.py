from collections import deque

# Initialize a deque
queue = deque()

# Add elements to the queue (enqueue)
queue.append(1)
queue.append(2)
queue.append(3)
print("Queue after enqueue:", queue)

# Remove elements from the queue (dequeue)
front_element = queue.popleft()
print("Dequeued element:", front_element)
print("Queue after dequeue:", queue)