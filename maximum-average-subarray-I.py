# Description:

#  Given an array consisting of n integers, find the contiguous subarray of given length k that has the maximum average value. And you need to output the maximum average value.

# Example:

# Input: [1,12,-5,-6,50,3], k = 4
# Output: 12.75
# Explanation: Maximum average is (12-5-6+50)/4 = 51/4 = 12.75

# Note:

# 1. 1 <= k <= n <= 30,000.
# 2. Elements of the given array will be in the range [-10,000, 10,000].


# Solution:
# python3

class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        A = [0]
        for x in nums:
            A.append(A[-1] + x)

        max_sum = max(A[i+k] - A[i] 
                 for i in range(len(nums) - k + 1))
        return max_sum / float(k)
