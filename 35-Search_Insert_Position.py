class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        index = 0
        for i, num in enumerate(nums):
            if num >= target:
                index = i
                return i
        
        if index == 0:
            return len(nums)