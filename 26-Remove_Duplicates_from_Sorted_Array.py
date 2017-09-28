class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        origin_len = len(nums)
        unique_index = 0
        
        if origin_len == 0:
            return 0
        
        for j in range(origin_len):
            if nums[unique_index] != nums[j]:
                unique_index = unique_index + 1
                nums[unique_index] = nums[j]


        return unique_index+1