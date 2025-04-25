class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

    
class LinkedList:
    def __init__(self):
        self.head = None
    def insert(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            
        else:
            temp = self.head
            while(temp.next):
                temp = temp.next
            new_node=Node(val)
            temp.next = new_node

    def display(self):
        result=[]
        temp = self.head
        while(temp):
            result.append(temp.data)
            temp = temp.next
        print("-->".join(map(str,result)))
    
    

l = LinkedList()
l.insert(70)
l.insert(506)   
l.insert(503)

l.display()    