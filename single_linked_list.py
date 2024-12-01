class Node:
    """Represents a single node in the linked list."""
    def __init__(self, data):
        self.data = data  # Store the node's data
        self.next = None  # Pointer to the next node


class SinglyLinkedList:
    """Implementation of a singly linked list."""
    def __init__(self):
        self.head = None  # Start with an empty list

    # 1. Insert at the beginning - O(1)
    def insert_at_beginning(self, data):
        new_node = Node(data)  # Create a new node
        new_node.next = self.head  # Point it to the current head
        self.head = new_node  # Update the head

    # 2. Insert at the end - O(n)
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:  # If the list is empty
            self.head = new_node
            return
        current = self.head
        while current.next:  # Traverse to the last node
            current = current.next
        current.next = new_node

    # 3. Insert after a specific node - O(n)
    def insert_after_node(self, target_data, data):
        current = self.head
        while current and current.data != target_data:  # Find the target node
            current = current.next
        if current is None:  # If target node not found
            raise ValueError(f"Node with data {target_data} not found.")
        new_node = Node(data)
        new_node.next = current.next
        current.next = new_node

    # 4. Delete a node by value - O(n)
    def delete_by_value(self, target_data):
        if self.head is None:  # If the list is empty
            return
        if self.head.data == target_data:  # If the head is the target
            self.head = self.head.next  # Remove the head
            return
        current = self.head
        while current.next and current.next.data != target_data:  # Find the node before the target
            current = current.next
        if current.next is None:  # Target node not found
            raise ValueError(f"Node with data {target_data} not found.")
        current.next = current.next.next  # Skip over the target node

    # 5. Search for a value - O(n)
    def search(self, key):
        current = self.head
        while current:
            if current.data == key:
                return True
            current = current.next
        return False

    # 6. Reverse the linked list - O(n)
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next  # Store the next node
            current.next = prev  # Reverse the link
            prev = current  # Move prev forward
            current = next_node  # Move current forward
        self.head = prev  # Update head to the new start

    # 7. Get the length of the linked list - O(n)
    def get_length(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    # 8. Display the linked list - O(n)
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


# Example Usage
if __name__ == "__main__":
    ll = SinglyLinkedList()
    ll.insert_at_beginning(10)
    ll.insert_at_end(20)
    ll.insert_at_end(30)
    ll.insert_after_node(20, 25)
    ll.display()  # Output: 10 -> 20 -> 25 -> 30 -> None
    ll.delete_by_value(25)
    ll.display()  # Output: 10 -> 20 -> 30 -> None
    ll.reverse()
    ll.display()  # Output: 30 -> 20 -> 10 -> None
    print("Length:", ll.get_length())  # Output: Length: 3
    print("Search 20:", ll.search(20))  # Output: Search 20: True
