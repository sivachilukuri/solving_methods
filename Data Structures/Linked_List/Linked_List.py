class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linked_List:

    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return 
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
    
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at(self, position, data):
        if position < 0:
            print("Invalid position")
            return 
        new_node = Node(data)
        if position == 0:
            new_node.next = self.head
            return
        curr = self.head
        count = 0
        while curr and count < position -1 :
            curr = curr.next
            count += 1
        if not curr:
            print("Position out of range")
            return 
        new_node.next = curr.next
        curr.next = new_node
    
    def delete_at(self, position):
        if not self.head:
            print("List is empty so cannot delete")
            return 
        if position < 0:
            print("Invalid Position")
            return 
        if position == 0:
            self.head = self.head.next
            return
        curr = self.head
        count = 0
        previous = None
        while curr and count < position:
            previous = curr
            curr = curr.next
            count += 1
        if not curr:
            print("Position out of range")
            return
        previous.next = curr.next
    
    def search(self, key):
        curr = self.head
        while curr:
            if curr.data == key:
                return True
            curr = curr.next
        return False

    def print_list(self):
        current = self.head
        while current:
            print(current.data,end="->")
            current = current.next
        print()

# Execution
l = Linked_List()
l.append(45)
l.append(75)
l.append(85)
l.prepend(65)
l.insert_at(2,55)
l.delete_at(0)
l.insert_at(2,65)
l.print_list()
print(l.search(45))
