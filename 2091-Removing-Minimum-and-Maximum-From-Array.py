class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        i = nums.index(min(nums))
        j = nums.index(max(nums))
        
        # Ensure i is the smaller index for simpler math
        if i > j:
            i, j = j, i
            
        n = len(nums)
        
        # Strategy 1: Remove both from the front
        front = j + 1
        
        # Strategy 2: Remove both from the back
        back = n - i
        
        # Strategy 3: Remove one from the front (up to i) and one from the back (down to j)
        both_sides = (i + 1) + (n - j)
        
        return min(front, back, both_sides)