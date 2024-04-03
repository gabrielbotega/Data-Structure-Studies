class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoubleLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next
    
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = self.tail = new_node
            self.length += 1
            return True
        temp = self.tail
        self.tail.next = new_node
        self.tail = new_node
        self.tail.prev = temp
        self.length += 1
        return True
    
    def pop(self):
        if self.head is None:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp
    
    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True
    
    def pop_first(self):
        if self.head is None:
            return None
        temp = self.head
        if self.length == 1:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.length -= 1
        return temp
    
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        middle = (self.length) // 2
        if index <= middle:
            temp = self.head
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range((self.length - 1) - index):
                temp = temp.prev
        return temp
    
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        new_node = Node(value)
        if index == 0:
            self.prepend(value)

        elif index == self.length:
            self.append(value)
        else:
            after = self.get(index)
            if after:
                before = after.prev
                new_node.prev = before
                new_node.next = after
                after.prev = new_node
                before.next = new_node
                self.length += 1
                return True
            return False
        return True
    
    def remove(self, index):
        if self.length == 0 or self.length == 1 or index == self.length:
            return self.pop()
        if index == 0:
            return self.pop_first()
        temp = self.get(index)
        if temp:
            after = temp.next
            before = temp.prev
            temp.next = temp.prev = None
            after.prev = before
            before.next = after
            return temp
        return None
                    
        

my_doubly_linked_list = DoubleLinkedList(0)
my_doubly_linked_list.append(1)
my_doubly_linked_list.append(2)
my_doubly_linked_list.append(3)
my_doubly_linked_list.append(4)
my_doubly_linked_list.append(5)
# my_doubly_linked_list.pop()

my_doubly_linked_list.print_list()

print("========== remove ===========")
my_doubly_linked_list.remove(6)
my_doubly_linked_list.print_list()



# print("========== PREPEND 0 ===========")
# my_doubly_linked_list.prepend(0)

# my_doubly_linked_list.print_list()

# print("========== POPFIST ===========")

# print(my_doubly_linked_list.pop_first())

# print("========== POPFIST ===========")
# print(my_doubly_linked_list.pop_first())

# print("========== POPFIST ===========")
# print(my_doubly_linked_list.pop_first())

# print("========== POPFIST ===========")
# print(my_doubly_linked_list.pop_first())


# print("========== POP 1 ===========")
# print(my_doubly_linked_list.pop())
# my_doubly_linked_list.print_list()

# print("========== POP 2 ===========")
# print(my_doubly_linked_list.pop())
# my_doubly_linked_list.print_list()

# print("========== POP 3 ===========")
# print(my_doubly_linked_list.pop())
# my_doubly_linked_list.print_list()
