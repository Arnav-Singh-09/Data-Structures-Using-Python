from collections import deque
import time
import threading

q = deque()
q.appendleft("First Element")
q.appendleft("Second Element")
q.appendleft("Third Element")
q.appendleft("Fourth Element")
print(q)

class Queue:
    def __init__(self):
        self.container = deque()
    def __str__(self):
        res = map(str,self.container)
        ret = 'Output Sequence : '
        ret += " -> ".join(res)
        return ret
    def enqueue(self,val):
        self.container.appendleft(val)
    def dequeue(self):
        return self.container.pop()
    def peek(self):
        return self.container[-1]
    def size(self):
        return len(self.container)
    def is_empty(self):
        return len(self.container) == 0

queue_obj = Queue()
for item in q:
    queue_obj.enqueue(item)
print(queue_obj)

orders = ['pizza','samosa','pasta','biryani','burger']
food_queue = Queue()

def place_order(orders):
    for item in orders:
        print("Placing order : ",item)
        food_queue.enqueue(item)
        time.sleep(0.5)

def serve_order():
    time.sleep(1.15)
    while food_queue.is_empty() is False:
        item = food_queue.dequeue()
        print("Serving : ",item)
        time.sleep(2.05)

t1 = threading.Thread(target= place_order, args= (orders,))
t2 = threading.Thread(target= serve_order)

t1.start()
t2.start()

t1.join()
t2.join()

print("All orders served !!!")