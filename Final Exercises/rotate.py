"""
List: Rotate ( ** Interview Question)
You are given a list of n integers and a non-negative integer k.

Your task is to write a function called rotate that takes the list of integers and an integer k as input and 
rotates the list to the right by k steps.

The function should modify the input list in-place, and you should not return anything.

Constraints:

Each element of the input list is an integer.

The integer k is non-negative.

Function signature: def rotate(nums, k):

Example:

Input: nums = [1, 2, 3, 4, 5, 6, 7], k = 3
Function call: rotate(nums, k)
Output: nums = [5, 6, 7, 1, 2, 3, 4]

Explanation: The list has been rotated to the right by 3 steps:

[7, 1, 2, 3, 4, 5, 6]

[6, 7, 1, 2, 3, 4, 5]

[5, 6, 7, 1, 2, 3, 4]
"""

"""
The problem about this exercise is thinking about a k bigger than len(nums). A way to deal with it is to
calculate the modulus of k with len(nums) -> k % len(nums). If k < len(nums) it will give the exactly amout to move
and if it's bigger (k>len()) it'll be wrapped up and will give the "similar" value to move. 

For example:
nums = [1, 2, 3]
k = 4

k % len(nums) = 1

therefore, with k = 4, with this array is the same as move only one step.
"""


def rotate(nums, k):
    k = k % len(nums)
    nums[:] = nums[-k:] + nums[:-k]



nums = [1, 2, 3, 4]
k = 2
rotate(nums, k)
print("Rotated array:", nums)

# nums = [1, 2, 3, 4, 5, 6, 7]
# k = 3
# rotate(nums, k)
# print("Rotated array:", nums)

# nums = [1, 2]
# k = 1
# rotate(nums, k)
# print("Rotated array:", nums)


"""
    EXPECTED OUTPUT:
    ----------------
    Rotated array: [5, 6, 7, 1, 2, 3, 4]

"""