class Solution(object):
    def validSequence(self, word1, word2):
        n = len(word1)
        m = len(word2)
        
        last_pos = [-1] * m
        
        ptr2 = m - 1
        for ptr1 in range(n - 1, -1, -1):
            if ptr2 >= 0 and word1[ptr1] == word2[ptr2]:
                last_pos[ptr2] = ptr1
                ptr2 -= 1
                
        res = []
        i = 0 
        j = 0 
        changed = False 
        
        while j < m:
            found = False
            while i < n:
                if word1[i] == word2[j]:
                    res.append(i)
                    i += 1
                    j += 1
                    found = True
                    break
                elif not changed:
                    if j == m - 1 or last_pos[j + 1] > i:
                        res.append(i)
                        i += 1
                        j += 1
                        changed = True
                        found = True
                        break
                i += 1
            
            if not found:
                return []
                
        return res