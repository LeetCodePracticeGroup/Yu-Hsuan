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
        if val not in nums:
            return length
        
        # sort
        for i in range(length - 1):
            if nums[i] == val:
                for j in range(i+1, length):
                    if nums[j] != val:
                        tmp = nums[i]
                        nums[i] = nums[j]
                        nums[j] = tmp
                        
        return nums.index(val)