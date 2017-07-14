# Description:

#  Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.

# Do not allocate extra space for another array, you must do this in place with constant memory.

# Example:

# Given input array nums = [1,1,2],

# Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. It doesn't matter what you leave beyond the new length. 


# Solution:
# python3

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
        	return 0
        a = 0
        for i in nums:
            if nums[i] != nums[a]:
                a += 1
            	nums[a] = nums[i]
        return a + 1
