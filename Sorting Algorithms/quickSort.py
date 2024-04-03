"""
BIG O: The Big O of the quick sort is the following: When running the pivot function we pass through all the elements in the array (O(n)). 
However, everytime we run the pivot we divide the array in half. And to run quickSort we run this log n times in n elements array.
Therefore, Big O of quickSort is: O(n log n). (THIS IS THE BEST CASE) If we already have the sorted data, after running the pivot function we'll only have data
on the right, and we'll run every element again and again. N x N. O(n²).


Since we're going to swap in two differente moments, I'm going to create a function for it.

Another point to note is that we're returning the INDEX of where the pivot is staying when sorted. Therefore, we're going to run the function again in the 
"left" array and "right" array.
"""

def swap(arr, index1, index2):
    temp = arr[index1]
    arr[index1] = arr[index2]
    arr[index2] = temp


def pivot(arr, pivotIndex, endIndex):
    swapIndex = pivotIndex

    for i in range(pivotIndex + 1, endIndex + 1):
        #here we're comparing values and swapping values
        if arr[i] < arr[pivotIndex]:
            swapIndex += 1
            swap(arr, swapIndex, i)

    swap(arr, pivotIndex, swapIndex)
    return swapIndex


def quickSortHelper(arr, leftIndex, rightIndex):
    if leftIndex < rightIndex:
        pivotIndex = pivot(arr, leftIndex , rightIndex) #this will return the index and the sides sorted
        quickSortHelper(arr, leftIndex, pivotIndex - 1)
        quickSortHelper(arr, pivotIndex + 1, rightIndex)

    return arr


def quickSort(arr):
    return quickSortHelper(arr, 0, len(arr) -1 )

arr = [4, 6, 1, 7, 3, 2, 5]

print(quickSort(arr))
# print(arr) #changed array  - Note that all the itens less than 4 is in the left and all those greater than 4 is in the right


