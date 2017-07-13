# Description

# Given a string, find the length of the longest substring without repeating characters.

# Example:

# Given "abcabcbb", the answer is "abc", which the length is 3.

# Given "bbbbb", the answer is "b", with the length of 1.

# Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.


# Solution:
# python3

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        substring = []
        max_len = 0
        for i in s:
            if i in substring:
                if len(substring) > max_len:
                    max_len = len(substring) 
                substring = substring[substring.index(i) + 1:]
            substring.append(i)
        if max_len > len(substring):
            return max_len
        return len(substring)

