class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        idxLeft = 0
        idxRight = len(numbers) - 1

        while idxLeft < idxRight:
            l = numbers[idxLeft]
            r = numbers[idxRight]
            sum = l + r
            if sum == target:
                return [idxLeft+1, idxRight+1]
            if sum < target:
                idxLeft += 1
            if sum > target:
                idxRight -= 1
