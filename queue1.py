
# Step 1: Create an empty list to represent the queue

queue1 = []
queue1.append(1)

queue1.append(2)
queue1.append(3)
queue1.append(4)
queue1.append(5)

#Dequeue (remove) the first element from the front of the list
dequeued_item = queue1.pop(0)
print("Dequeued:", dequeued_item)

#peek item 
if len(queue1)>0 :
    print("front item:",queue1[0])
else:
    print("empty queue")


if len(queue1)==0 :
    print("empty queue") 

else:
    print("the queue is:",queue1)       




 #using queue module in python
import queue   

q1 = queue.Queue()

q1.put(10)

q1.put(20)
q1.put(30)
q1.put(40)

#Dequeue an element
dequeued_item = q1.get()
print("Dequeued:", dequeued_item)


#Peek at the first element without removing it
#use of empty
if not q1.empty():
    front_item = q1.queue[0]
    print("Front item:", front_item)
else:
    print("Queue is empty")

# Step 5: Check if the queue is empty
if q1.empty():
    print("Queue is empty")
else:
    print("Queue is not empty")





