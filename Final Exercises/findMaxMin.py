"""
List: Find Max Min ( ** Interview Question)
Write a Python function that takes a list of integers as input and returns a tuple containing the maximum and
minimum values in the list.

The function should have the following signature:

def find_max_min(myList):


Where myList is the list of integers to search for the maximum and minimum values.

The function should traverse the list and keep track of the current maximum and minimum values. It should then 
return these values as a tuple, with the maximum value as the first element and the minimum value as the second element.

For example, if the input list is [5, 3, 8, 1, 6, 9], the function should return (9, 1) since 9 is the maximum value and 1 is the
 minimum value.
"""


# 1) maybe the best way to implement this is to use Heap. O(n logn)
class Heap:
    def __init__(self):
        self.heapMax = []
        self.heapMin = []

    def __leftChild(self, index):
        return 2 * index + 1

    def __rightChild(self, index):
        return 2 * index + 2

    def __parent(self, index):
        return (index - 1) // 2
    
    def __swapMax(self, index1, index2):
        self.heapMax[index1], self.heapMax[index2] = self.heapMax[index2], self.heapMax[index1]

    def __swapMin(self, index1, index2):
        self.heapMin[index1], self.heapMin[index2] = self.heapMin[index2], self.heapMin[index1]

    def insertMax(self, value):
        self.heapMax.append(value)

        current = len(self.heapMax) - 1

        while current > 0 and  self.heapMax[current] > self.heapMax[self.__parent(current)]:
            self.__swapMax(current, self.__parent(current))
            current = self.__parent(current)
        

    def insertMin(self, value):
        self.heapMin.append(value)

        current = len(self.heapMin) - 1

        while current > 0 and  self.heapMin[current] < self.heapMin[self.__parent(current)]:
            self.__swapMin(current, self.__parent(current))
            current = self.__parent(current)
    
def maxMinHeap(arr):
    heap = Heap()
    for i in arr:
        heap.insertMin(i)
        heap.insertMax(i)
    return (heap.heapMax[0], heap.heapMin[0])

# 2) or I can use sorting - quick and sort or merge and sort O(n logn)
def maxMinMerge(arr):
    if len(arr) == 1:
        return (arr[0], arr[0])
    if len(arr) > 1:

        mid = len(arr) // 2

        L = arr[:mid]
        R = arr[mid:]

        maxMinMerge(L)
        maxMinMerge(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i+=1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i+=1
            k+=1

        while j < len(R):
            arr[k] = R[j]
            j+=1
            k+=1

        return (arr[-1], arr[0])
            

# 3) maybe use swap and pointer technique O(n)

def maxMinPointers(arr):
    maxIndex = minIndex = 0

    for index, val in enumerate(arr):
        if val > arr[maxIndex]:
            maxIndex = index
        
        if val < arr[minIndex]:
            minIndex = index

    return (arr[maxIndex], arr[minIndex])


print( maxMinMerge([5, 3, 8, 1, 6, 9]) )
print( maxMinHeap([5, 3, 8, 1, 6, 9]) )
print( maxMinPointers([5, 3, 8, 1, 6, 9]) )


"""
    EXPECTED OUTPUT:
    ----------------
    (9, 1)
    
"""