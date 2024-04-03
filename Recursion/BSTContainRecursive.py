class Node: 
    def __init__(self, value):
        self.value = value
        self.right = self.left = None

class Tree:
    def __init__(self):
        self.root = None

    def __r_insert(self, currentNode, value):
        if currentNode == None:
           return Node(value)
        if value < currentNode.value:
           currentNode.left = self.__r_insert(currentNode.left, value)
        if value > currentNode.value:
           currentNode.right = self.__r_insert(currentNode.right, value)
        return currentNode
        
    def __r_contains(self, currentNode, value):
        if currentNode == None:
            return False
        if value == currentNode.value:
            return True
        if value > currentNode.value:
            return self.__r_contains(currentNode.right, value)
        if value < currentNode.value:
            return self.__r_contains(currentNode.left, value)
    
    def r_contains(self, value):
        return self.__r_contains(self.root, value)
    
    def r_insert(self, value):
        if self.root is None:
            self.root = Node(value)
        self.__r_insert(self.root, value)

    def __deleteNode(self,currentNode, value):
        # 1) If the value you're trying to delete is not in the BST
        if currentNode == None:
            return None
        
        # 2) Traverse through the BST searching the desired value to delete
        if value < currentNode.value:
            currentNode.left = self.__deleteNode(currentNode.left, value)
        elif value > currentNode.value:
            currentNode.right = self.__deleteNode(currentNode.right, value)

        # 3) If you've found the value
        else:
            # I do have 4 options here:
            # 1) leaf node (child) with no children
            if currentNode.left is None and currentNode.right is None:
                return None

            # 2) Opening on the right (have a smaller child)
            elif currentNode.right is None:
                currentNode = currentNode.left
            
            # 3) Opening on the left (have a bigger child)
            elif currentNode.left is None:
                currentNode = currentNode.right
            
            # 4) Has no opening
            else:
                # Here I allocate the minimin value of the right subtree (child).
                min_subtree = self.min_value(currentNode.right)
                currentNode.value = min_subtree
                currentNode.right = self.__deleteNode(currentNode.right, min_subtree)
        #need to return the stacks, that's why I need this return here
        return currentNode
    
    def min_value(self, currentNode):
        while currentNode.left is not None:
            currentNode = currentNode.left
        return currentNode.value


    def deleteNode(self, value):
        return self.__deleteNode(self.root, value)
        
    

myTree = Tree()
# myTree.r_insert(47)
# myTree.r_insert(21)
# myTree.r_insert(76)
# myTree.r_insert(18)
# myTree.r_insert(27)
# myTree.r_insert(52)
# myTree.r_insert(82)

myTree.r_insert(2)
myTree.r_insert(1)
myTree.r_insert(3)

"""
       2
      / \
     1   3 
"""


print("Root: ", myTree.root.value)
print("Left Node: ", myTree.root.left.value)
print("Right Node: ", myTree.root.right.value)

print("is there 3?", myTree.r_contains(3))

print("========= Delete 2 =========")
myTree.deleteNode(2)

"""
       3
      / \
     1   None
"""


print("Root: ", myTree.root.value)
print("Left Node: ", myTree.root.left.value)
print("Right Node: ", myTree.root.right)

