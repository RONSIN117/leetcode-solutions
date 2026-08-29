class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)
        if n == 0:
            return []
            
        sorted_nums = sorted([(num, i) for i, num in enumerate(nums)])
        
        res = [0] * n
        i = 0
        
        while i < n:
            j = i + 1
            while j < n and sorted_nums[j][0] - sorted_nums[j-1][0] <= limit:
                j += 1
            
            indices = sorted([sorted_nums[k][1] for k in range(i, j)])
            for k in range(i, j):
                res[indices[k - i]] = sorted_nums[k][0]
            
            i = j
            
        return res