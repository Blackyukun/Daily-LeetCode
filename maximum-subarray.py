# Description:

#  Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

# Example:

# Given the array [-2,1,-3,4,-1,2,1,-5,4],
# the contiguous subarray [4,-1,2,1] has the largest sum = 6. 


# Solution:
# python3

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        nowsum = maxsum = nums[0]
        for i in nums[1:]:
            nowsum = max(i, nowsum+i)
            maxsum = max(nowsum, maxsum)
        
        return maxsum

