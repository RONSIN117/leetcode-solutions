class Solution(object):
    def lengthOfLongestSubstring(self, s):
        char_index = {}
        max_len = 0
        left = 0
        
        for right in range(len(s)):
            if s[right] in char_index:
                left = max(char_index[s[right]], left)
            
            max_len = max(max_len, right - left + 1)
            char_index[s[right]] = right + 1
            
        return max_len