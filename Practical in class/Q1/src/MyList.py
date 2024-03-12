from Car import *
from Node import *
class MyList:
    def __init__(self):
        self.head = None
        self.tail = None
    def isEmpty(self):
        return self.head ==None
    def traverse(self):
        pt = self.head
        while pt:
            print(pt.data, end = " ")
            pt = pt.next
        print("")        
    def clear(self):
        self.head = None
#Q1-1
    def addLast(self, name="", price=-1):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        if name[0] != 'B' and price <= 100:
            if self.head is None:
                new_node = Node(Car(name, price))
                self.head = new_node
            else:
                pointer = self.head
                while pointer.next is not None:
                    pointer = pointer.next
                self.tail = pointer
                new_node = Node(Car(name, price))
                pointer.next = new_node

    # end def
#Q1-2    
    def addFirst(self, name="", price=-1):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        new_node = Node(Car(name, price))
        new_node.next = self.head
        self.head = new_node
        
    # end def
#Q1-3
    def delete(self, price =0):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        if self.head.data.Price == price:
            self.head = self.head.next
        else:
            pointer = self.head
            while pointer.next.next is not None:
                if pointer.next.data.Price == price:
                    break
                else:
                    pointer = pointer.next
            pointer.next = pointer.next.next
        
    #end def
# Q1-4
    def sort(self):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        if self.head is None:
            return None
        
        while True:
            pointer = self.head
            change = 0
            
            while pointer.next is not None:
                if pointer.data.Price > pointer.next.data.Price:
                    pointer.data, pointer.next.data = pointer.next.data, pointer.data
                    change += 1
                pointer = pointer.next
            
            if change == 0:
                break 
    #end def    