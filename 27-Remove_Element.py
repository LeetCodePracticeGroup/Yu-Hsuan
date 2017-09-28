class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        
        length = len(nums)
        
        if length == 0:
            return 0
        
        i = 0
        for j in range(length):
            if nums[j] != val:
                nums[i] = nums[j]
                i = i + 1
                
        return i