class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        k = k1 + k2
        diffs = [abs(a - b) for a, b in zip(nums1, nums2)]
        
        if sum(diffs) <= k:
            return 0
            
        max_d = max(diffs)
        freq = [0] * (max_d + 1)
        for d in diffs:
            freq[d] += 1
            
        for d in range(max_d, 0, -1):
            if freq[d] > 0:
                take = min(freq[d], k)
                freq[d] -= take
                freq[d - 1] += take
                k -= take
                if k == 0:
                    break
                    
        return sum(d * d * count for d, count in enumerate(freq) if count > 0)