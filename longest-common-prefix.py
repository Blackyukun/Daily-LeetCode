# Description:

# Write a function to find the longest common prefix string amongst an array of strings. 

# Example:

# ['leetcode','leetco','leet','lee']
# return 'lee'


# Solution:
# python3

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        for i in range(len(strs[0])):
            for string in strs[1:]:
                if i >= len(string) or string[i] != strs[0][i]:
                    return strs[0][:i]
        return strs[0]

