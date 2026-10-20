class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        sorted_nums = sorted(nums)
        
        def is_rotation(text, pattern):
            m = len(pattern)
            if m == 0:
                return True
            
            # Compute LPS (Longest Prefix Suffix) array for KMP
            lps = [0] * m
            j = 0
            for i in range(1, m):
                while j > 0 and pattern[i] != pattern[j]:
                    j = lps[j-1]
                if pattern[i] == pattern[j]:
                    j += 1
                    lps[i] = j
                    
            # KMP matching
            j = 0
            for i in range(len(text)):
                while j > 0 and text[i] != pattern[j]:
                    j = lps[j-1]
                if text[i] == pattern[j]:
                    j += 1
                if j == m:
                    return True
            return False

        def check(k):
            for i in range(0, n, k):
                orig = nums[i:i+k]
                targ = sorted_nums[i:i+k]
                
                # Check if orig can be rotated to targ using KMP
                if not is_rotation(orig + orig, targ):
                    return False
            return True

        total_sum = 0
        for k in range(1, int(n**0.5) + 1):
            if n % k == 0:
                if check(k):
                    total_sum += k
                if k != n // k:
                    if check(n // k):
                        total_sum += (n // k)
                        
        return total_sum