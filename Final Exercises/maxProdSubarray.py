"""
The idea here is to test every subarray possible.
"""

class Solution(object):
    def maxProduct(self, nums):
        ans = float("-inf")
        prefix = suffix = 1
        n = len(nums)

        for i in range(n):
            if prefix == 0:
                prefix = 1
            if suffix == 0:
                suffix = 1
            
            prefix *= nums[i]
            suffix *= nums[n-i-1]

            ans = max(ans, max(prefix, suffix))

        return ans



maxProdSubarray = Solution()

print(maxProdSubarray.maxProduct([-2,0,-1]))
