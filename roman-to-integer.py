# Description:

# Given a roman numeral, convert it to an integer.

# Input is guaranteed to be within the range from 1 to 3999.


# Solution:
# python3

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman = {'M': 1000,'D': 500 ,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1}
        a = 0
        for i in range(0, len(s) - 1):
            if roman[s[i]] < roman[s[i+1]]:
                a -= roman[s[i]]
            else:
                a += roman[s[i]]
        return a + roman[s[-1]]
