"""
Find out if there is repeated occurrences in the two given lists.
"""

def findRepeated(arr1, arr2):
    myDict = {}
    for item in arr1:
        myDict[item] = True
    for i in arr2:
        if i in myDict:
            return True
    return False


arr1 = [1, 2, 3, 4, 5]
arr2 = [7,8,9,10,55]

print(findRepeated(arr1, arr2))