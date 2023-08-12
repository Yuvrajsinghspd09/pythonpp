class stack3():
    def __init__(self) :
        self.items = []

    def checkisempty1(self):
        return len(self.items)==0
    
    def pushfunc1(self,item):
        return self.items.append(item)
    
    def popfunc1(self):
        if len(self.items )>0:
            self.items.pop()

        else:
            return "cannot pop"


    def peekfunc1(self):
        if len(self.items)==0:
            return "top is -1"
        else :
            return self.items[-1]
        



mystack3 = stack3()

mystack3.pushfunc1(5)
mystack3.popfunc1()
mystack3.pushfunc1(6)

print("Peek:", mystack3.peekfunc1())
