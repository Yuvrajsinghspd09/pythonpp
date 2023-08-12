#implementing queue using class
class queue1:
    def __init__(self) :
        self.items=[]

    def enqueue1(self,item):
        self.items.append(item)

    def is_empty(self):
        return len(self.items) == 0

    def dequeue1(self):
        if not self.is_empty:
          self.items.pop()    
        else:
            return None
        

    
    def peek1(self):
        if not self.is_empty():
            return self.items[0]
        else:
            return None    
        



q = queue1()
q.enqueue1(100)
q.enqueue1(200)
q.enqueue1(300)

print("Front item:", q.peek1())

dequeued_item = q.dequeue1()
print("Dequeued:", dequeued_item)

print("Is queue empty?", q.is_empty())