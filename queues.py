class Queues:
    def __init__(self,list) -> None:
        self.list = list

    def addq(self,elem):
        self.list.insert(0,elem)
    
    def removeq(self) -> any:
        return self.list.pop()
    
    def __str__(self) -> str:
        return ", ".join([str(i) for i in self.list])