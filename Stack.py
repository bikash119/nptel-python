class Stack:
    def __init__(self,list):
        self.list = list
    
    def push(self,elem) -> ():
        self.list.append(elem)

    def pop(self) -> any:
        return self.list.pop()

    def __str__(self):
        return ".".join([str(i) for i in self.list])