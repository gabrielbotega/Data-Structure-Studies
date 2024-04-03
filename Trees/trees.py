class Node:
    def __init__(self, value):
        self.value = value
        self.left = self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        newNode = Node(value)
        if self.root is None:
            self.root = newNode
            return True
        temp = self.root
        while temp:
            if newNode.value == temp.value:
                return False
            if newNode.value > temp.value:
                if temp.right is None:
                    temp.right = newNode
                    return True
                temp = temp.right
            else:
                if temp.left is None:
                    temp.left = newNode
                    return True
                temp = temp.left

    def contains(self, value):
        temp = self.root
        while temp:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False



my_tree = BinarySearchTree()
# my_tree.insert(2)
# my_tree.insert(1)
# my_tree.insert(3)
# my_tree.insert(24)
# my_tree.insert(13)
# my_tree.insert(35)


# print("======= TREE =======")
# print(my_tree.root.value)
# print(my_tree.root.left.value)
# print(my_tree.root.right.value)

print("======= Contains =======")
print(my_tree.contains(44))