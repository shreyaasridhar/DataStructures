class Stack:
    def __init__(self):
        self.items=[]
    def push(self,ele):
        self.items.append(ele)
    def pop(self):
        return(self.items.pop())
    def size(self):
        return(len(self.items))
    def is_empty(self):
        return(self.items==[])
    def top(self):
        return(self.items[-1])
