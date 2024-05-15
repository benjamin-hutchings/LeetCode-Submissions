class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        res = 0
        l, r = 0, len(height) - 1

        while l < r:
            area = (r - l) * min(height[l],height[r])
            res = max(res, area)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        
        return res


        # BRUTE FORCE SOLUTION:
        # largest_area = 0

        # # Define the area calculation function
        # def area(idx_left, idx_right):
        #     container_height = min(height[idx_left], height[idx_right])
        #     return container_height * (idx_right - idx_left)

        # # Iterate through all pairs of indices to find the maximum area
        # for i in range(len(height)):
        #     for j in range(i + 1, len(height)):
        #         current_area = area(i, j)
        #         if current_area > largest_area:
        #             largest_area = current_area

        # return largest_area