class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        first = {}
        last = {}
        
        for i, c in enumerate(s):
            if c not in first:
                first[c] = i
            last[c] = i
            
        def get_valid_right(i):
            right = last[s[i]]
            j = i
            while j <= right:
                if first[s[j]] < i:
                    return -1
                right = max(right, last[s[j]])
                j += 1
            return right

        intervals = []
        for i in range(len(s)):
            if i == first[s[i]]:
                right = get_valid_right(i)
                if right != -1:
                    intervals.append((i, right))
                    
        intervals.sort(key=lambda x: x[1])
        
        res = []
        prev_right = -1
        
        for left, right in intervals:
            if left > prev_right:
                res.append(s[left:right + 1])
                prev_right = right
                
        return res