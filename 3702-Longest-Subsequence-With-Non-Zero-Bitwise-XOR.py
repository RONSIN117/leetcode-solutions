class Solution(object):
    def longestSubsequence(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total_xor = 0
        all_zero = True
        
        for x in nums:
            total_xor ^= x
            if x != 0:
                all_zero = False
                
        if all_zero:
            return 0
            
        if total_xor != 0:
            return len(nums)
            
        return len(nums) - 1