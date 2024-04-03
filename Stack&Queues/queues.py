class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self, value):
        newNode = Node(value)
        self.first = newNode
        self.last = newNode
        self.length = 1

    def print_queue(self):
        temp = self.first
        while temp:
            print(temp.value)
            temp = temp.next

    def enqueue(self, value):
        newNode = Node(value)
        if self.first is None:
            self.first = self.last = newNode
        else:
            self.last.next = newNode
            self.last = newNode
        self.length += 1
        return True        
    
    def dequeue(self):
        if self.first is None:
            return None
        temp = self.first
        if self.length == 1:
            self.first = self.last = None
        else:
            self.first = self.first.next
            temp.next = None
        self.length -= 1
        return temp

            
myQueue = Queue(4)
myQueue.enqueue(7)

myQueue.print_queue()

print("======= dequeue =======")
print(myQueue.dequeue())
print("======= dequeue =======")
print(myQueue.dequeue())
print("======= dequeue =======")
print(myQueue.dequeue())

print("======= List =======")
myQueue.print_queue()