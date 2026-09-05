class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        
        suf_min = [0] * n
        suf_min[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            suf_min[i] = min(suf_min[i + 1], nums[i])
            
        pref_max = float('-inf')
        
        for i in range(n):
            pref_max = max(pref_max, nums[i])
            if pref_max - suf_min[i] <= k:
                return i
                
        return -1