class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail=None



    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head:
            new_node.next = self.head
            self.head = new_node
        else:
            self.head = new_node
            self.tail=new_node


    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head:
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.tail = new_node
            self.head=new_node
    
    def search(self, data):
        current_node = self.head
        while current_node:
            if current_node.data == data:
                return True
            current_node = current_node.next
        return False
    
    def printLinkedList(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    #a. remove_beginning(self)
    def remove_beginning(self):
        if not self.head:
            return None
        removed_data = self.head.data
        self.head = self.head.next
        if not self.head:
            self.tail = None
        return removed_data

    #b. remove_at_end(Self)
    def remove_at_end(self):
        if not self.head:
            return None
        if self.head == self.tail:
            removed_data = self.head.data
            self.head = None
            self.tail = None
            return removed_data

        current = self.head
        while current.next != self.tail:
            current = current.next

        removed_data = self.tail.data
        self.tail = current
        self.tail.next = None
        return removed_data

    #c. remove_at(self, data)
    def remove_at(self, data):
        if not self.head:
            return None

        if self.head.data == data:
            return self.remove_beginning()

        current = self.head
        while current.next:
            if current.next.data == data:
                removed_data =current.next.data
                if current.next ==self.tail:
                    self.tail = current
                current.next = current.next.next
                return removed_data
            current = current.next

        return None

    #d. insert_after(self, nodedata, data)
    def insert_after(self, nodedata, data):
        current = self.head
        while current:
            if current.data == nodedata:
                new_node = Node(data)
                new_node.next = current.next
                current.next = new_node
                if current == self.tail:
                    self.tail = new_node
                return data
            current = current.next
        return None
  



if __name__ == "__main__":
    ll = LinkedList()
    for value in [10, 20, 30]:
        ll.insert_at_end(value)
    ll.printLinkedList()