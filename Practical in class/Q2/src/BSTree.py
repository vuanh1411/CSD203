from Car import *
from Node import *
class NodeQ:
    def __init__(self,data):
        self.data = data
        self.next = None
class MyQueue:
    def __init__(self):
        self.head = None
        self.tail = None
    def isEmpty(self):
        return self.head ==None
    def EnQueue(self, data):
        node = NodeQ(data)
        if self.isEmpty():
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
    #end def
    def DeQueue(self):
        if self.isEmpty():
            return None
        data = self.head.data
        self.head = self.head.next
        return data
#end class    
class BSTree:
    def __init__(self):
        self.root = None
    # end def
    def clear(self):
        self.root = None
    def isEmpty(self):
        return self.root == None
    #end def
    def insert(self,name, price):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        new_node=Node(Car(name,price))
        if name[0]=='B' or price>100:
            return
        else:
            if self.root is None:
                self.root=new_node
            else:
                cur=self.root
                father=None
                while cur:
                    if cur.data.Price==price:
                        return
                    elif cur.data.Price>price:
                        father=cur
                        cur=cur.left
                    else:
                        father=cur
                        cur=cur.right
                if father.data.Price>price:
                    father.left=new_node
                elif father.data.Price<price:
                    father.right=new_node
                
        #########################
        pass
    #end def
    def visit(self,p):
        if p==None:
            return
        print(f"{p.data}",end =" ")
    #end def
    def preOrder(self,p):
        if p==None:
            return
        self.visit(p)
        self.preOrder(p.left)
        self.preOrder(p.right)
    #end def
    def preVisit(self):
        self.preOrder(self.root)
        print("")
    #end def
    def postOrder(self,p):
        if p==None:
            return
        self.postOrder(p.left)
        self.postOrder(p.right)
        self.visit(p)
    #end def
    def postVisit(self):
        self.postOrder(self.root)
        print("")
    #end def
    def inOrder(self,p):
        if p==None:
            return
        self.inOrder(p.left)
        self.visit(p)
        self.inOrder(p.right)        
    #end def
    def inVisit(self):
        self.inOrder(self.root)
        print("")
    #end def
    def breadth_first(self):
        if self.isEmpty():
            return
        my = MyQueue()
        my.EnQueue(self.root)
        while not my.isEmpty():
            p = my.DeQueue()
            print(f"({p.data.Name},{p.data.Price})", end=" ")
            if p.left != None:
                my.EnQueue(p.left)
            if p.right != None:
                my.EnQueue(p.right)
        print("")  # Print a new line after each level of the tree
        #end def
    def f2(self):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        def preOrder2(p):
            if p==None:
                return
            if 3<=p.data.Price<=5:
                self.visit(p)
            preOrder2(p.left)
            preOrder2(p.right)
        preOrder2(self.root)
        print()
        ####################
        pass
    def breadth_first(self):
        if self.root is None:
            return
        queue = MyQueue()
        queue.EnQueue(self.root)
        while not queue.isEmpty():
            current = queue.DeQueue()
            print(f"({current.data.Name},{current.data.Price})", end=" ")
            if current.left:
                queue.EnQueue(current.left)
            if current.right:
                queue.EnQueue(current.right)

    def f3(self):
        flag = True
        count = 0
        deleteNode = None

        def check(x):
            return x < 7

        def breadth_first2(tree):
            nonlocal deleteNode, flag, count
            if tree.isEmpty():
                return
            my = MyQueue()
            my.EnQueue(tree.root)
            while not my.isEmpty():
                p = my.DeQueue()
                if (p.left != None and p.right != None and check(p.data.Price) and flag):
                    deleteNode = p
                    count += 1
                    if count == 1:
                        flag = False
                        break
                if p.left != None:
                    my.EnQueue(p.left)
                if p.right != None:
                    my.EnQueue(p.right)
        def deleteByCopyingLeft(p):
            if p == None or p.left == None:
                return
            if p.left.right == None:
                p.data = p.left.data
                p.left = p.left.left
                return
            cur = p.left.right
            father = p.left
            while cur.right:
                father = cur
                cur = cur.right
            p.data = cur.data
            father.right = cur.left

        # Perform breadth-first traversal to find and delete the node
        breadth_first2(self)
        deleteByCopyingLeft(deleteNode)
        print()
        #############################    
        pass
    def f4(self):
        flag = True
        rotate_node = None
        count = 0
        
        def check(x):
            return x < 7
        
        def breadth_first3(tree):
            if tree.isEmpty():
                return
            my = MyQueue()
            my.EnQueue(tree.root)
            while not my.isEmpty():
                p = my.DeQueue()
                nonlocal rotate_node, count, flag
                if p.left is not None and check(p.data.Price) and flag:
                    rotate_node = p
                    count += 1
                    if count == 1:
                        flag = False
                        break
                if p.left is not None:
                    my.EnQueue(p.left)
                if p.right is not None:
                    my.EnQueue(p.right)
        
        def findFather(tree, data):
            if tree.root.data.Price == data:
                return None  
            fa = None  
            cur = tree.root
            while cur:            
                if cur.data.Price == data:
                    return fa
                fa = cur    
                if cur.data.Price < data:
                    cur = cur.right
                else:
                    cur = cur.left
            return None  
        
        def rightRotate(p):        
            if not p or not p.left:
                return
            c = p.left
            p.left = c.right
            c.right = p
            return c 
        
        def rightRotation(tree, data):
            nonlocal rotate_node
            f = findFather(tree, data.Price)        
            p = None
            if f is None:
                if tree.root.data != data:
                    return
                else:
                    p = tree.root
            else:
                if f.data.Price > data.Price:
                    p = f.left
                else:
                    p = f.right  
            newNode = rightRotate(p) 
            if f is None:
                tree.root = newNode
            else:
                if f.data.Price < data.Price:
                    f.right = newNode
                else:
                    f.left = newNode
        
        breadth_first3(self)
        if rotate_node is not None:
            rightRotation(self, rotate_node.data)
        print()
        #################################
        pass


# end class
