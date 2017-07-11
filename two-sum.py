# Description:

# Given an array of integers, return indices of the two numbers such that they add up to a specific target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# Example:

# Given nums = [2, 7, 11, 15], target = 9,

# Because nums[0] + nums[1] = 2 + 7 = 9,

# return [0, 1].


# Solution:
# python3

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}
        for e, i in enumerate(nums):
            if target-i in dict:
                return [dict[target-i], e]
            dict[i] = e

    def twoSum2(self, nums, target):
    	"""
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        k = 0
        for i in nums:
            k += 1
            new_nums = nums[k:]
            if target - i in new_nums:
                return [k - 1, new_nums.index(target - i) + k]
