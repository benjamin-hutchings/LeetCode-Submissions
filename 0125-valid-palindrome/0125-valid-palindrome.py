class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        newStr = []

        for idx in s:
            if idx.isalnum():
                newStr += idx.lower()

        return newStr == newStr[::-1]