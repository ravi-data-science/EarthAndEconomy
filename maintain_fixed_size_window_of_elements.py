from collections import deque

# Initialize a deque with a maximum length of 3
window = deque(maxlen=3)

# Add elements to the deque
window.append(1)
print("Window:", window)

window.append(2)
print("Window:", window)

window.append(3)
print("Window:", window)

# Add another element, automatically removes the oldest element
window.append(4)
print("Window after adding 4:", window)