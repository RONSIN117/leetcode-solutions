class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        from collections import Counter
        
        avail = Counter(s)
        best_i = -1
        
        for j in range(len(target)):
            for char_code in range(ord(target[j]) + 1, ord('z') + 1):
                if avail[chr(char_code)] > 0:
                    best_i = j
                    break 
            
            if avail[target[j]] > 0:
                avail[target[j]] -= 1
            else:
                break 
        if best_i == -1:
            return ""
            
        avail = Counter(s)
        res = []
        for k in range(best_i):
            res.append(target[k])
            avail[target[k]] -= 1
        for char_code in range(ord(target[best_i]) + 1, ord('z') + 1):
            c = chr(char_code)
            if avail[c] > 0:
                res.append(c)
                avail[c] -= 1
                break
        for char_code in range(ord('a'), ord('z') + 1):
            c = chr(char_code)
            while avail[c] > 0:
                res.append(c)
                avail[c] -= 1
                
        return "".join(res)