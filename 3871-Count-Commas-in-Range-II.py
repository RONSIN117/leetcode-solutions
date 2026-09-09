class Solution:
    def countCommas(self, n: int) -> int:
        total_commas = 0
        power_of_1000 = 1000
        
        while power_of_1000 <= n:
            total_commas += (n - power_of_1000 + 1)
            power_of_1000 *= 1000
            
        return total_commas