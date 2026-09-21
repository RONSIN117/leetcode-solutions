from typing import List

class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        result = [0] * k
        curr_dp = {}
        
        for num in nums:
            next_dp = {}
            next_dp[num % k] = 1
            
            for r, count in curr_dp.items():
                new_r = (r * num) % k
                next_dp[new_r] = next_dp.get(new_r, 0) + count
                
            for r, count in next_dp.items():
                result[r] += count
                
            curr_dp = next_dp
            
        return result