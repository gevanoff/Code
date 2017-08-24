class Queue2Stacks(object):
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        
    def enqueue(self,element):
        while len(self.stack2) != 0:
            self.stack1.append(self.stack2.pop())
        self.stack1.append(element)
        
    def dequeue(self):
        while len(self.stack1) != 0:
            self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

q = Queue2Stacks()

for i in range(5):
    q.enqueue(i)

for i in range(5):
    print(q.dequeue())
