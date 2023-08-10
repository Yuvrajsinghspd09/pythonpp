#implement a function to reverse a string using a stack in Python

class stack2():
    def __init__(self):
        self.items=[]
        
    def isemptyfunc(self):
        return len(self.items)==0
    
    def pushfunc(self,item):
        self.items.append(item)

    def popfunc(self):
        if not self.isemptyfunc():
            return self.items.pop()
        else:
            return "stack is empty"
        


def myrevstring(input_string):
      mystack2 = stack2()

      for char in input_string:
        mystack2.pushfunc(char)

      revstring = ""
      while not mystack2.isemptyfunc():
       revstring += mystack2.popfunc()
      return revstring
       


# Testing the reverse_string function
original_string = input("enter a string")
reversed_result = myrevstring(original_string)
print("Original:", original_string)
print("Reversed:", reversed_result)       

