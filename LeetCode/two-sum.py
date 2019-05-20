class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        solutions = {}
        for index, num in enumerate(nums):
            if target - num in solutions:
                return [solutions[target - num], index]
            solutions[num] = index
