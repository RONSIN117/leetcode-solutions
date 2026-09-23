from typing import List

class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        n_orig = len(nums)
        n = 1
        while n < n_orig:
            n *= 2
            
        tree_tot = [1] * (2 * n)
        tree_cnt = [[0] * k for _ in range(2 * n)]
        
        for i in range(n_orig):
            val = nums[i] % k
            tree_tot[n + i] = val
            tree_cnt[n + i][val] = 1
            
        for i in range(n_orig, n):
            tree_tot[n + i] = 1
            
        for i in range(n - 1, 0, -1):
            left = 2 * i
            right = 2 * i + 1
            tree_tot[i] = (tree_tot[left] * tree_tot[right]) % k
            
            tree_cnt[i][:] = tree_cnt[left]
            
            ltot = tree_tot[left]
            for j, c in enumerate(tree_cnt[right]):
                if c:
                    tree_cnt[i][(ltot * j) % k] += c
                    
        res = []
        for idx, val, start_i, x_i in queries:
          
            p = n + idx
            v = val % k
            tree_tot[p] = v
            for j in range(k):
                tree_cnt[p][j] = 0
            tree_cnt[p][v] = 1
            
            p //= 2
            while p > 0:
                left = 2 * p
                right = 2 * p + 1
                tree_tot[p] = (tree_tot[left] * tree_tot[right]) % k
                
                tree_cnt[p][:] = tree_cnt[left]
                ltot = tree_tot[left]
                for j, c in enumerate(tree_cnt[right]):
                    if c:
                        tree_cnt[p][(ltot * j) % k] += c
                p //= 2
                
            L = n + start_i
            R = n + n_orig - 1
            
            left_nodes = []
            right_nodes = []
            
            while L <= R:
                if L % 2 == 1:
                    left_nodes.append(L)
                    L += 1
                if R % 2 == 0:
                    right_nodes.append(R)
                    R -= 1
                L //= 2
                R //= 2
                
            ans = 0
            running_tot = 1
            
            for node in left_nodes + right_nodes[::-1]:
                for j, c in enumerate(tree_cnt[node]):
                    if c and (running_tot * j) % k == x_i:
                        ans += c
                running_tot = (running_tot * tree_tot[node]) % k
                
            res.append(ans)
            
        return res