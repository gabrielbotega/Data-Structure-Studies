#This is the code that I wrote
def bubbleSort(arr):
    k = 1
    while len(arr) - k > 0:
        for i in range(len(arr)-k):
            if arr[i] > arr[i+1]:
                temp = arr[i+1]
                arr[i+1] = arr[i]
                arr[i] = temp
        k += 1
    return arr

#This is the professors code
def bubble_sort(arr):
    for i in range(len(arr) - 1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                temp = arr[j+1]
                arr[j+1] = arr[j]
                arr[j] = temp
    return arr




arr = [2,4,1,3,6,8,7,5]

print(bubbleSort(arr))
print(bubble_sort(arr))
