class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def display(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    def delete_node(self, bid):
        current_node = self.head
        prev_node = None
        while current_node:
            if current_node.data.split(" | ")[0] == bid:
                if prev_node:
                    prev_node.next = current_node.next
                else:
                    self.head = current_node.next
                return True
            prev_node = current_node
            current_node = current_node.next
        return False
