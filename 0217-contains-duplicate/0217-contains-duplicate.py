class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        # # Bruteforce: Time = O(n^2), Space = O(1).
        # left = 0
        # right = 0

        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         left = nums[i]
        #         right = nums[j]
        #         if left == right:
        #             return True
        #         else:
        #             pass

        # Optimised: Time = O(n), Space = O(n)
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
            
        return False