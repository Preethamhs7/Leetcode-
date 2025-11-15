class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
 
        index_position = {}  
        for i, num in enumerate(nums):
            diff = target - num
            if diff in index_position:
                return [index_position[diff], i]
            index_position[num] = i

