# class Node:
class Node: 
    def __init__(self, value):
        self.value = value
        self.next = None
        
# class LinkedList:
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True
    
    def pop(self):
        if self.head is None:
            return None
        elif self.head.next is None:
            temp = self.head
            self.head = None
            self.tail = None
        else:
            temp = self.head
            while temp.next is not self.tail:
                temp = temp.next
            self.tail = temp
            temp = self.tail.next
            self.tail.next = None
        self.length -= 1
        return print(temp.value)
    
    def prepend(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        if self.length == 0:           
            self.tail = new_node
        self.length += 1
        return True

    def pop_first(self):
        temp = self.head
        if self.head is None:
            return None
        self.head = self.head.next
        temp.next = None
        if self.head is None:
            self.tail = None
        self.length -=1
        return print(temp.value)
    
    def get(self, index):
        if index > self.length or self.length is None or index < 0:
            return False
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
    
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    def insert(self, index, value):
        if index > self.length or index < 0:
            return False
        new_node = Node(value)
        temp = self.head
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        temp = self.get(index-1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True
    
    def remove(self, index):
        if index >= self.length or index < 0:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length-1:
            return self.pop()
        pre = self.get(index-1)
        # temp = self.get(index)  O(N)
        temp = pre.next # O(1) 
        pre.next = temp.next
        temp.next = None
        self.length -= 1
        return temp
    
    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after
        return True

     
        
 
my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)

print("====== My original LL ======")
my_linked_list.print_list()

print("====== My reversed LL ======")
my_linked_list.reverse()
my_linked_list.print_list()



# print("====== My INSERTED LIST ======")
# my_linked_list.insert(3,55)
# my_linked_list.print_list()

# print("====== My REMOVED LIST ======")
# removed = my_linked_list.remove(3)
# my_linked_list.print_list()

# print("====== My REMOVED ITEM ======")
# print(removed.value)


# print("====== My seted LL ======")
# my_linked_list.set_value(3,50)
# my_linked_list.print_list()




# print("====== My get element LL ======")
# my_linked_list.get(1)


# print("====== My Pops ======")
# my_linked_list.pop()
# my_linked_list.pop()
# my_linked_list.pop()
# my_linked_list.pop()
# my_linked_list.pop()


# my_linked_list.prepend(0)
# print("====== My prepended LL ======")
# my_linked_list.print_list()

# my_linked_list.append(1)
# print("====== My appended LL ======")
# my_linked_list.print_list()

# my_linked_list.pop_first()
# print("====== My poped-first LL ======")

# my_linked_list.pop_first()
# print("====== My poped-first LL ======")
# my_linked_list.pop_first()
# print("====== My poped-first LL ======")


# print('Head:', my_linked_list.head.value)
# print('Tail:', my_linked_list.tail.value)
# print('Length:', my_linked_list.length)


"""
    EXPECTED OUTPUT:
    ----------------
    Head: 4
    Tail: 4
    Length: 1
    
"""

                                                                                                                    