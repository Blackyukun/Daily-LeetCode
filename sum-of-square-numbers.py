# Description:

# Given a non-negative integer c, your task is to decide whether there're two integers a and b such that a2 + b2 = c. 

# Example 1:

# Input: 5
# Output: True
# Explanation: 1 * 1 + 2 * 2 = 5

# Example2:

# Input: 3
# Output: False


# Solution:
# python3

class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        return any(c - a*a == int((c - a*a) ** 0.5) ** 2 for a in range(int(c ** 0.5) + 1))
