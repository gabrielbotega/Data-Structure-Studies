# My solution
def selectionSort(arr):
    k = 0
    while k < len(arr) -1:
        minIndex = k
        for i in range(k, len(arr)-1):
            if arr[minIndex] > arr[i+1]:
                minIndex = i+1
        temp = arr[k]
        arr[k] = arr[minIndex]
        arr[minIndex] = temp
        k += 1
    return arr


#professor solution
def selection_sort(arr):
    for i in range(len(arr)-1):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j
        if i != min_index:
            temp = arr[i]
            arr[i] = arr[min_index]
            arr[min_index] = temp
    
    return arr


arr = [2,4,1,3,6,8,7,5]

print(selectionSort(arr))
print(selection_sort(arr))