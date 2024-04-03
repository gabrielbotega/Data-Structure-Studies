# this will be the constructor for a MaxHeap starting from zero.

class MaxHeap:
    def __init__(self):
        self.heap = []

    def _left_child(self, index):
        return 2*index + 1
    
    def _right_child(self, index):
        return 2*index + 2
    
    def _parent(self, index):
        return (index - 1 ) // 2
    
    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def _sink_down(self, index):
        max_index = index

        while True:

            left_index = self._left_child(index)
            right_index = self._right_child(index)

            #Need to account the possibility to not have a value. The _child support method returns a value (a index, indepedently if exists),
            # it does not check if there is a value in the spot.
            if left_index < len(self.heap) and self.heap[left_index] > self.heap[max_index]:
                max_index = left_index
            
            if right_index < len(self.heap) and self.heap[right_index] > self.heap[max_index]:
                max_index = right_index

            if index != max_index:
                self._swap(index, max_index)
                index = max_index
            else:
                return

    def insert(self, value):
        self.heap.append(value)
        # last index
        current = len(self.heap) - 1
        while current > 0 and self.heap[current] > self.heap[self._parent(current)]:
            self._swap(self._parent(current), current)
            current = self._parent(current)

    def remove(self):
        if len(self.heap) == 0:
            return None
        
        if len(self.heap) == 1:
            return self.heap.pop()
        
        #need to pop the biggest value in the end
        max_value = self.heap[0]

        #Need to make the heap complete again
        self.heap[0] = self.heap.pop()

        self._sink_down(0)

        return max_value
        
        
print("===== Inserting Values =====")
heap = MaxHeap()
heap.insert(99)
heap.insert(72)
heap.insert(61)
heap.insert(58)

print(heap.heap)

print("===== Inserting Values (100) =====")
heap.insert(100)
print(heap.heap)

print("===== Inserting Values (75) =====")
heap.insert(75)

print(heap.heap)

print("===== Removing Value =====")
heap.remove()

print(heap.heap)