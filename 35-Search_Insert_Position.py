class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        l = 0
        r = len(nums) - 1

        # binary search
        while l <= r:
            middle = (l+r) / 2

            if nums[middle] > target:
                r = middle - 1
            elif nums[middle] < target:
                l = middle + 1
            else:
                return middle

        return l