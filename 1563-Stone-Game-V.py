from typing import List

class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        n = len(stoneValue)
        
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stoneValue[i]
            
        def get_sum(i, j):
            return prefix[j + 1] - prefix[i]

        dp = [[0] * n for _ in range(n)]
        
        max_l = [[0] * n for _ in range(n)]
        
        max_r = [[0] * n for _ in range(n)]

        for i in range(n):
            max_l[i][i] = stoneValue[i]
            max_r[i][i] = stoneValue[i]

        for i in range(n - 1, -1, -1):
            mid = i 
            for j in range(i + 1, n):
                total_sum = get_sum(i, j)
                
                while mid < j and get_sum(i, mid) * 2 < total_sum:
                    mid += 1
                
                res = 0
                
                if get_sum(i, mid) * 2 == total_sum:
                    res = max(max_l[i][mid], max_r[mid + 1][j])
                else:
                    if mid > i:
                        res = max(res, max_l[i][mid - 1])
                    if mid < j:
                        res = max(res, max_r[mid + 1][j])
                
                dp[i][j] = res
                
                max_l[i][j] = max(max_l[i][j - 1], total_sum + dp[i][j])
                max_r[i][j] = max(max_r[i + 1][j], total_sum + dp[i][j])

        return dp[0][n - 1]