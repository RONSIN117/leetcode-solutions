# Python
class Solution:
    def stoneGameIII(self, stoneValue):
        n = len(stoneValue)
        dp = [float('-inf')] * n + [0]
        
        for i in range(n - 1, -1, -1):
            take = 0
            for k in range(1, 4):
                if i + k - 1 < n:
                    take += stoneValue[i + k - 1]
                    dp[i] = max(dp[i], take - dp[i + k])
                    
        if dp[0] > 0:
            return "Alice"
        elif dp[0] < 0:
            return "Bob"
        else:
            return "Tie"