class Node:
    def __init__(self, data):
        self.data = data  # Store the value
        self.next = None  # Pointer to the next node

class LinkedList:
    def __init__(self):
        self.head = None  # Initially, the linked list is empty

    # Function to insert a new node at the end of the list
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    # Function to print the linked list
    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")

    # Function to reverse the linked list
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next  # Store the next node
            current.next = prev  # Reverse the current node's pointer
            prev = current  # Move the prev pointer one step forward
            current = next_node  # Move the current pointer one step forward
        self.head = prev  # Set the new head of the list



if __name__ == '__main__':
    # Create a linked list
    llist = LinkedList()

    # Append elements to the linked list
    llist.append(1)
    llist.append(2)
    llist.append(3)
    llist.append(4)

    # Print original list
    print("Original Linked List:")
    llist.print_list()  # Output: 1 -> 2 -> 3 -> 4 -> None

    # Reverse the linked list
    llist.reverse()

    # Print reversed list
    print("Reversed Linked List:")
    llist.print_list()  # Output: 4 -> 3 -> 2 -> 1 -> None

    