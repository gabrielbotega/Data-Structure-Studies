"""
Stack: Implement Stack Using a List ( ** Interview Question)
In the Stack: Intro video we discussed how stacks are commonly implemented using a list instead of a linked list.

Create a constructor for Class Stack that implements a new stack with an empty list called stack_list.
"""

class Stack:
    def __init__(self):
        self.stack_list = []

    def printStackList(self):
        for i in range(len(self.stack_list)):
            print(self.stack_list[(len(self.stack_list)-1) - i])
    
    def push(self, value):
       self.stack_list.append(value)

    def pop(self):
        if not any(self.stack_list):
            return None
        return self.stack_list.pop()
    
myStack = Stack(4)
myStack.push(11)
myStack.push(55)

myStack.printStackList()

print("======== POP ==========")
print(myStack.pop())


print("======== Stack ==========")
myStack.printStackList()