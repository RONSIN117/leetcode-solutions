class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        import bisect
        
        n = len(intervals)
        arr = [(intervals[i][0], intervals[i][1], intervals[i][2], i) for i in range(n)]
        
        arr.sort(key=lambda x: x[0])
        starts = [x[0] for x in arr]
        
        next_idx = [n] * n
        for i in range(n):
            next_idx[i] = bisect.bisect_right(starts, arr[i][1])
            
        dp = [[(0, ())] * 5 for _ in range(n + 1)]
        
        for i in range(n - 1, -1, -1):
            for k in range(1, 5):
                skip = dp[i + 1][k]
                
                nxt = next_idx[i]
                take_score = arr[i][2] + dp[nxt][k - 1][0]
                take_tuple = tuple(sorted(dp[nxt][k - 1][1] + (arr[i][3],)))
                
                if take_score > skip[0]:
                    dp[i][k] = (take_score, take_tuple)
                elif take_score == skip[0]:
                    if take_tuple < skip[1]:
                        dp[i][k] = (take_score, take_tuple)
                    else:
                        dp[i][k] = skip
                else:
                    dp[i][k] = skip
                    
        return list(dp[0][4][1])