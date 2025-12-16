class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def insert_at_head(self, data):
        """Insert a new node at the beginnging of the list"""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1
    
    def insert_at_tail(self, data):
        """Insert a new node at the end of the list"""
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            self.size += 1
            return
        
        current = self.head
        while current.next: #while next exists - loop through list
            current = current.next
        current.next = new_node # assigns end node with new node
        self.size += 1 #increase counter 

    def delete(self, data):
        """Delete the first occurance of a node with given data"""
        if not self.head: # checks if node in linked list exists
            return False 
        
        #If head needs to be deleted
        if self.head.data == data:
            self.head = self.head.next
            self.size -= 1
            return True
        
        current = self.head
        while current.next: #while next exists 
            if current.next.data == data:
                current.next = current.next.next
                self.size -= 1
                return True
            current = current.next #loop to next if current.next.data != data:
        return False
    
    def search(self, data):
        """Search for a node with given data"""
        current = self.head
        while current: #while current exists
            if current.data == data:
                return True
            current = current.next
        return False 
    
    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return  " -> ".join(elements)
    
    # Example usage
if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_at_tail(1)
    ll.insert_at_tail(2)
    ll.insert_at_tail(3)
    ll.insert_at_head(0)
    
    print(ll.display())  # Output: 0 -> 1 -> 2 -> 3
    print(ll.search(2))  # Output: True
    ll.delete(2)
    print(ll.display())  # Output: 0 -> 1 -> 3