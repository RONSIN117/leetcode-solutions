from typing import List
import collections

class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        row_masks = collections.defaultdict(int)
        
        for row, seat in reservedSeats:
            if 2 <= seat <= 9:
                row_masks[row] |= (1 << (seat - 2))
                
        max_groups = (n - len(row_masks)) * 2
        
        for mask in row_masks.values():
            if (mask & 15) == 0 and (mask & 240) == 0:
                max_groups += 2
            elif (mask & 15) == 0 or (mask & 240) == 0 or (mask & 60) == 0:
                max_groups += 1
                
        return max_groups