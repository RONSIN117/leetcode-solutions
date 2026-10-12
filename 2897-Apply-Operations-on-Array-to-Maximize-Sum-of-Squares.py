from typing import List

class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        counts = [0] * 32
        
        for num in nums:
            for i in range(32):
                if (num >> i) & 1:
                    counts[i] += 1
                    
        ans = 0
        for _ in range(k):
            val = 0
            for i in range(32):
                if counts[i] > 0:
                    val |= (1 << i)
                    counts[i] -= 1
            ans = (ans + val * val) % MOD
            
        return ans