#implement a stack using an array (list) in Python
class Stack1:

    def __init__(self):
        self.items = []


    def isemptyfunc(self):
        return len(self.items)==0
    

    def pushfunc(self,item) :
        self.items.append(item)

    def popfunc(self):
        if not self.isemptyfunc():
            return self.items.pop()
        else:
            return "stack is empty, cannot pop"
        
    def peekfunc(self):
        if not self.isemptyfunc():
            return self.items[-1]
        else:
            return "stack is empty, cannot peek"
        

    def sizefunc(self):
        return len(self.items)    



    
    
mystack1 = Stack1()
mystack1.pushfunc(4)

mystack1.pushfunc(5)

mystack1.pushfunc(6)

print("Peek:", mystack1.peekfunc())

print("Size:", mystack1.sizefunc())
print("Pop:", mystack1.popfunc())

print("Pop:", mystack1.popfunc())

print("Is Empty:", mystack1.isemptyfunc())  
print("Size:", mystack1.sizefunc())

print("Pop:", mystack1.popfunc())    
print("Is Empty:", mystack1.isemptyfunc()) 
