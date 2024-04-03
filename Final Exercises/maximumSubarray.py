"""
Given an integer array nums, find the subarray with the largest sum, and return its sum.

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
Example 2:

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.

Input: nums = [-2,-1]
Output: -1
Explanation: The subarray [-1] has the largest sum -1.
"""

class Solution(object):
    def maxSubArray(self, nums):
        if len(nums) == 0:
            return 0

        maxSum = float("-inf")
        currSum = 0

        for val in nums:
            currSum += val

            if currSum > maxSum:
                maxSum = currSum

            if currSum < 0:
                currSum = 0

        return maxSum




teste = Solution()

print(teste.maxSubArray([-2,-1]))