class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7
        ends_with = [0] * 26
        total = 0
        
        for char in s:
            idx = ord(char) - ord('a')
            old_val = ends_with[idx]
            
            new_val = (total + 1) % MOD
            
            ends_with[idx] = new_val
            
            total = (total + new_val - old_val) % MOD
            
        return total