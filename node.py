class Node:
    # Initialize a node
    def __init__(self,value=None):
        '''
        Usage : 
        newnode = Node() # will create a node with value as None
        newnode = Node(a) # will create a node with value as a
        '''
        self.value = value
        self.next = None 
  
    # Check if the list is empty
    def isempty(self):
        '''
            if value of first element is empty, then we term the list as empty list
        '''
        return(self.value == None)

    # Append a element to the list recursively
    def append(self,value):
        if self.isempty():
            self.value = value
        elif self.next == None:
            node = Node(value)
            self.next = node
        else:
            self.next.append(value)

    # Append a element to the list iteratively
    def appendi(self,value):
        # Empty List
        if self.isempty():
            self.value = value
            return
        # Singleton Node. A list with only 1 node
        elif self.next == None:
            node = Node(value)
            self.next = node
        else:
            while self.next != None:
                self = self.next
            node = Node(value)
            self.next = node
            return

    # Recursively find length of the list
    def lenr(self) -> (int):
        if self.isempty():
            return 0
        elif self.next == None:
            return 1
        else:
            return 1+ self.next.lenr()

    # Iteratively find the length of list
    def leni(self)-> (int):
        if self.isempty():
            return 0
        # singleton node. a list with only 1 node
        elif self.next == None:
            return 1
        else:
            len = 0
            while self.next != None:
                len +=1
                self = self.next
            len += 1
        return len

    # Insert an element to head of the list
    def insert(self,value):
        # Empty List
        if self.isempty():
            self.value = value
        # List with one or more node. Singleton list
        else:
            newnode = Node(value)
            (newnode.value,self.value) = (self.value,newnode.value)
            (newnode.next,self.next) = (self.next,newnode)
    # delete a node by index
    def deletei(self,index) -> (int,bool):
        '''
        Usage : l.delete(0)
        '''
        length = self.leni()
        # Empty list
        if self.isempty():
            print("Cannot delete anything from empty list")
            return (-1,False)
        elif index > length -1:
            print (f"Cannot delete element with index {index} from a list of size {length}")
            return (-1,False)
        # Removing the first element
        elif index == 0:
            (self.value,self.next.value) = (self.next.value,self.value)
            self.next = self.next.next
        elif self.next == None:
            value = self.value
            self.value = None
            return (value,True)
        else:
            current_index = 0
            while self.next.next != None:
                if current_index == index:
                    break
                else:
                    current_index +=1
                    self = self.next
            value = self.value
            self.next = self.next.next
            return (value,True)
            
                

        # List with one node


        # List with more than one node

    def __str__(self):
        elems = []
        # Empty list
        if self.isempty():
            return str([])
        # Singleton Node. A list with only 1 Node.
        elif self.next == None:
            return str([self.value])
        else:
            while self.next != None:
                elems.append(self.value)
                self = self.next
            elems.append(self.value)
        return str(elems)

# Write test cases in order to 
    # 1. test all scenarios
    # 2. enable code coverage
l = Node()
l.append(5)
print(l) # Should print [5]
print(l.leni()) # should print 1
l.appendi(4)
print(l) # should print [5,4]
print(l.lenr()) # should print 2
l.insert(12)
print(l)
l.append(11)
l.deletei(0)
l.deletei(2)