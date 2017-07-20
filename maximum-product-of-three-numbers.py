# Description:

# Given an integer array, find three numbers whose product is maximum and output the maximum product.

# Example 1:

# Input: [1,2,3]
# Output: 6

# Example 2:

# Input: [1,2,3,4]
# Output: 24

# Note:

# The length of the given array will be in range [3,104] and all elements are in the range [-1000, 1000].
# Multiplication of any three numbers in the input won't exceed the range of 32-bit signed integer.


# Solution:
# python3

# Sort the array. Any "middle" numbers not in the first 3 or last 3 cannot be used in the final answer. If we are using a middle number, it must have both a left-neighbor and a right-neighbor, and switching to one of these neighbors will increase the product.

class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        if len(nums) > 6:
            nums = nums[:3] + nums[-3:]

        return max(nums[i] * nums[j] * nums[k]
                   for i in range(len(nums))
                   for j in range(i+1, len(nums))
                   for k in range(j+1, len(nums)))

