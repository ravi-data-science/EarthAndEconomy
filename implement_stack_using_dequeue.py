from collections import deque

# Initialize a deque
stack = deque()

# Add elements to the stack (push)
stack.append(1)
stack.append(2)
stack.append(3)
print("Stack after push:", stack)

# Remove elements from the stack (pop)
top_element = stack.pop()
print("Popped element:", top_element)
print("Stack after pop:", stack)