class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        left = 0
        ones_count = 0
        best_str = ""
        
        for right in range(len(s)):
            if s[right] == '1':
                ones_count += 1
            
            while ones_count == k:
                current_len = right - left + 1
                if not best_str or current_len < len(best_str):
                    best_str = s[left:right+1]
                elif current_len == len(best_str):
                    best_str = min(best_str, s[left:right+1])
                if s[left] == '1':
                    ones_count -= 1
                left += 1
                
        return best_str