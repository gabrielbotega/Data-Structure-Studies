def insertionSort(arr):
    for i in range(1, len(arr)):
        while i-1 >= 0 and arr[i] < arr[i-1]:
            temp = arr[i]
            arr[i] = arr[i-1]
            arr[i-1] = temp
            i -= 1

    return arr



arr = [3,5,2,4,6,8,7,1]

print(insertionSort(arr))