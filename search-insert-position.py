# Description:

# Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# You may assume no duplicates in the array.

# Example:

# Here are few examples.
# [1,3,5,6], 5 → 2
# [1,3,5,6], 2 → 1
# [1,3,5,6], 7 → 4
# [1,3,5,6], 0 → 0 


# Solution:
# python3
# The first is my solution.My runtime beats 95.83 % % of python submissions.
# The second is other's solution.
# The third is oyther's one liner solution.

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        a, b = 0, len(nums)
        while a < b:
        	if nums[0] >= target:
        		return a

        	elif nums[-1] < target:
        		return b

        	elif nums[a] < target and nums[a+1] >= target:
        		return a + 1
        	
        	else:
        		a += 1
    
    def searchInsert2(self, nums, target):
    	left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) / 2
            if nums[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1

        return left

    def searchInsert3(self, nums, target):
    	return len([x for x in nums if x<target])
