import math
from typing import List

class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        coins.sort()
        filtered_coins = []
        for c in coins:
            if not any(c % x == 0 for x in filtered_coins):
                filtered_coins.append(c)
                
        n = len(filtered_coins)
        pie_data = []
        
        for mask in range(1, 1 << n):
            current_lcm = 1
            bits = 0
            
            for i in range(n):
                if (mask >> i) & 1:
                    current_lcm = math.lcm(current_lcm, filtered_coins[i])
                    bits += 1
            
            sign = 1 if bits % 2 == 1 else -1
            pie_data.append((current_lcm, sign))
            
        left = 1
        right = k * filtered_coins[0]
        
        while left < right:
            mid = (left + right) // 2
            
            count = sum(sign * (mid // lcm_val) for lcm_val, sign in pie_data)
            
            if count >= k:
                right = mid  
            else:
                left = mid + 1
                
        return left