from collections import defaultdict

class Solution(object):
    def largestInteger(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        
        if k == n:
            return max(nums)
        if k == 1:
            counts = defaultdict(int)
            for x in nums:
                counts[x] += 1
            ans = -1
            for x, count in counts.items():
                if count == 1:
                    ans = max(ans, x)
            return ans
        counts = defaultdict(int)
        for x in nums:
            counts[x] += 1
            
        ans = -1
        if counts[nums[0]] == 1:
            ans = max(ans, nums[0])
        if counts[nums[-1]] == 1:
            ans = max(ans, nums[-1])
            
        return ans