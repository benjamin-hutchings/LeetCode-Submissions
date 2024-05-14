class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        res = []
        nums.sort()  # Sort the list to use two-pointer technique

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i-1]:
                continue  # Skip duplicates for the first element

            l, r = i + 1, len(nums) - 1  # Two pointers initialization
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum < 0:
                    l += 1  # Move left pointer right to increase the sum
                elif threeSum > 0:
                    r -= 1  # Move right pointer left to decrease the sum
                else:  # threeSum == 0
                    res.append([a, nums[l], nums[r]])  # Append the current triplet
                    l += 1
                    r -= 1
                    # Skip duplicates for the second and third elements
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
        return res
