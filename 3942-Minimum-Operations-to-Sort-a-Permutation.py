from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        
        ans = float('inf')
        
        k = nums[0]
        valid_S = True
        for i in range(n):
            if nums[i] != (k + i) % n:
                valid_S = False
                break
        
        if valid_S:
            dist = 0 if k == 0 else min(n - k, k + 2)
            ans = min(ans, dist)
            
        k = (nums[0] + 1) % n
        valid_R = True
        for i in range(n):
            if nums[i] != (k - 1 - i) % n:
                valid_R = False
                break
                
        if valid_R:
            dist = min(k + 1, n - k + 1)
            ans = min(ans, dist)
            
        return ans if ans != float('inf') else -1