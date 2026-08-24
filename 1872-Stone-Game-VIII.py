from typing import List

class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        n = len(stones)
        current_prefix_sum = sum(stones)
        max_diff = current_prefix_sum
        
        for i in range(n - 2, 0, -1):
            current_prefix_sum -= stones[i + 1]
            max_diff = max(max_diff, current_prefix_sum - max_diff)
            
        return max_diff