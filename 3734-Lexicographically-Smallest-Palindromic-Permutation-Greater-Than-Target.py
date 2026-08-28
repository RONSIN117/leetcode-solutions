class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        from collections import Counter
        
        n = len(s)
        counts = Counter(s)
        
        odd_count = sum(1 for v in counts.values() if v % 2 != 0)
        if odd_count > (n % 2):
            return ""
            
        mid = ""
        half_avail = {}
        for char, count in counts.items():
            if count % 2 != 0:
                mid = char
            if count // 2 > 0:
                half_avail[char] = count // 2
                
        t_half = target[:n // 2]
        
        possible_divergences = []
        avail = half_avail.copy()
        matched = True
        
        for i in range(n // 2):
            best_c = None
            for char_code in range(ord(t_half[i]) + 1, ord('z') + 1):
                c = chr(char_code)
                if avail.get(c, 0) > 0:
                    best_c = c
                    break
            if best_c:
                possible_divergences.append((i, best_c))
                
            if avail.get(t_half[i], 0) > 0:
                avail[t_half[i]] -= 1
            else:
                matched = False
                break
                
        if matched:
            exact_p = t_half + mid + t_half[::-1]
            if exact_p > target:
                return exact_p
                
        if not possible_divergences:
            return ""
            
        best_i, best_c = possible_divergences[-1]
        
        avail = half_avail.copy()
        half = []
        
        for i in range(best_i):
            half.append(t_half[i])
            avail[t_half[i]] -= 1
            
        half.append(best_c)
        avail[best_c] -= 1
        
        rem = []
        for char in sorted(avail.keys()):
            rem.extend([char] * avail[char])
            
        half.extend(rem)
        
        half_str = "".join(half)
        return half_str + mid + half_str[::-1]