class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        i = nums.index(min(nums))
        j = nums.index(max(nums))
        
        if i > j:
            i, j = j, i
            
        n = len(nums)
        
        front = j + 1
        
        back = n - i
        both_sides = (i + 1) + (n - j)
        
        return min(front, back, both_sides)