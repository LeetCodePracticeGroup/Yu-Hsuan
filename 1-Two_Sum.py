class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        for id, num in enumerate(nums):
        	sub = target - num
        	if sub != num and sub in nums:
        		return [id, nums.index(sub)]