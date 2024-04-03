# Here we're going to implement the Breath First Search algorithm

class Node:
    def __init__(self, value):
        self.value = value
        self.right = self.left = None

class BST:
    def __init__(self):
        self.root = None
    
    def __r_insert(self, currentNode, value):
        if currentNode is None:
            return Node(value)

        if value < currentNode.value:
            currentNode.left = self.__r_insert(currentNode.left, value)
        if value > currentNode.value:
            currentNode.right = self.__r_insert(currentNode.right, value)

        return currentNode
    
    def r_insert(self, value):
        if self.root is None:
            self.root = Node(value)
        self.__r_insert(self.root, value)

    def BFS(self):
        currentNode = self.root
        queue = []
        results = []
        queue.append(currentNode)
        while len(queue) > 0:
            currentNode = queue.pop(0)
            results.append(currentNode.value)
            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)

        return results
    
    def dfs_pre_order(self):
        results = []
        
        def traverse(currentNode):
            results.append(currentNode.value)
            if currentNode.left is not None:
                traverse(currentNode.left)
            if currentNode.right is not None:
                traverse(currentNode.right)
        
        traverse(self.root)
        return results

    def dfs_post_order(self):
        results = []
        
        def traverse(currentNode):
            if currentNode.left is not None:
                traverse(currentNode.left)
            if currentNode.right is not None:
                traverse(currentNode.right)
            results.append(currentNode.value)
        
        traverse(self.root)
        return results

    def dfs_in_order(self):
        results = []
        
        def traverse(currentNode):
            if currentNode.left is not None:
                traverse(currentNode.left)
            results.append(currentNode.value)
            if currentNode.right is not None:
                traverse(currentNode.right)
        
        traverse(self.root)
        return results
    
    
myTree = BST()
myTree.r_insert(47)
myTree.r_insert(21)
myTree.r_insert(76)
myTree.r_insert(18)
myTree.r_insert(27)
myTree.r_insert(52)
myTree.r_insert(82)


print(myTree.BFS())
print(myTree.dfs_pre_order())
print(myTree.dfs_post_order())
print(myTree.dfs_in_order())