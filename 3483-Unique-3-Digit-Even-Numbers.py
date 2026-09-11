class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        from typing import List

class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        digit_count = [0] * 10
        for digit in digits:
            digit_count[digit] += 1
            
        total_distinct_numbers = 0
        
        for num in range(100, 1000, 2):
            d1 = num // 100
            d2 = (num // 10) % 10
            d3 = num % 10
            
            req_count = [0] * 10
            req_count[d1] += 1
            req_count[d2] += 1
            req_count[d3] += 1
            
            if (digit_count[d1] >= req_count[d1] and 
                digit_count[d2] >= req_count[d2] and 
                digit_count[d3] >= req_count[d3]):
                total_distinct_numbers += 1
                
        return total_distinct_numbers