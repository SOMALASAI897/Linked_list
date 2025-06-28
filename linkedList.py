class Node:
    """
    A class to represent a node in the linked list.
    """
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """
    A class to represent a singly linked list with various operations.
    """
    def __init__(self):
        self.head = None
        self.size = 0
    
    def append(self, data):
        """
        Add a node to the end of the list.
        
        Args:
            data: The data to be stored in the new node
        """
        new_node = Node(data)
        
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        
        self.size += 1
    
    def print_list(self):
        """
        Print all elements in the list.
        """
        if not self.head:
            print("List is empty")
            return
        
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        
        print(" -> ".join(elements))
    
    def delete_nth_node(self, n):
        """
        Delete the nth node from the list (1-based indexing).
        
        Args:
            n (int): The position of the node to delete (1-based)
        
        Raises:
            ValueError: If the list is empty or index is out of range
        """
        # Check if list is empty
        if not self.head:
            raise ValueError("Cannot delete from an empty list")
        
        # Check if index is valid
        if n < 1 or n > self.size:
            raise ValueError(f"Index {n} is out of range. List has {self.size} elements")
        
        # If deleting the first node
        if n == 1:
            self.head = self.head.next
            self.size -= 1
            return
        
        # Find the node before the one to be deleted
        current = self.head
        for i in range(n - 2):  # n-2 because we want the node before nth node
            current = current.next
        
        # Delete the nth node
        node_to_delete = current.next
        current.next = node_to_delete.next
        self.size -= 1
    
    def get_size(self):
        """
        Get the current size of the list.
        
        Returns:
            int: The number of nodes in the list
        """
        return self.size
    
    def is_empty(self):
        """
        Check if the list is empty.
        
        Returns:
            bool: True if the list is empty, False otherwise
        """
        return self.head is None


def test_linked_list():
    """
    Test function to demonstrate the linked list functionality.
    """
    print("=== Linked List Implementation Test ===\n")
    
    # Create a new linked list
    ll = LinkedList()
    
    # Test 1: Adding elements
    print("1. Adding elements to the list:")
    elements = [10, 20, 30, 40, 50]
    for element in elements:
        ll.append(element)
        print(f"   Added {element}")
    
    print(f"   List size: {ll.get_size()}")
    print("   Current list:")
    ll.print_list()
    print()
    
    # Test 2: Delete middle node
    print("2. Deleting 3rd node (value 30):")
    try:
        ll.delete_nth_node(3)
        print("   Successfully deleted 3rd node")
        print("   Current list:")
        ll.print_list()
        print(f"   List size: {ll.get_size()}")
    except ValueError as e:
        print(f"   Error: {e}")
    print()
    
    # Test 3: Delete first node
    print("3. Deleting 1st node:")
    try:
        ll.delete_nth_node(1)
        print("   Successfully deleted 1st node")
        print("   Current list:")
        ll.print_list()
        print(f"   List size: {ll.get_size()}")
    except ValueError as e:
        print(f"   Error: {e}")
    print()
    
    # Test 4: Delete last node
    print("4. Deleting last node:")
    try:
        ll.delete_nth_node(ll.get_size())  # Delete last node
        print("   Successfully deleted last node")
        print("   Current list:")
        ll.print_list()
        print(f"   List size: {ll.get_size()}")
    except ValueError as e:
        print(f"   Error: {e}")
    print()
    
    # Test 5: Try to delete with invalid index
    print("5. Attempting to delete with invalid index (10):")
    try:
        ll.delete_nth_node(10)
        print("   Successfully deleted node at index 10")
    except ValueError as e:
        print(f"   Error: {e}")
    print()
    
    # Test 6: Delete all remaining nodes
    print("6. Deleting all remaining nodes:")
    while not ll.is_empty():
        try:
            ll.delete_nth_node(1)
            print(f"   Deleted node. Remaining size: {ll.get_size()}")
        except ValueError as e:
            print(f"   Error: {e}")
            break
    
    print("   Final list:")
    ll.print_list()
    print()
    
    # Test 7: Try to delete from empty list
    print("7. Attempting to delete from empty list:")
    try:
        ll.delete_nth_node(1)
        print("   Successfully deleted from empty list")
    except ValueError as e:
        print(f"   Error: {e}")


if __name__ == "__main__":
    test_linked_list()