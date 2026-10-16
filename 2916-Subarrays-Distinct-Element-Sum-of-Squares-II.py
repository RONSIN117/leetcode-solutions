class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        last_seen = {}
        
        sum2 = [0] * (4 * n)
        sum1 = [0] * (4 * n)
        lazy = [0] * (4 * n)
        
        def push(node, l, r):
            if lazy[node] != 0:
                val = lazy[node]
                mid = (l + r) // 2
                
                left_len = mid - l + 1
                right_len = r - mid
                
                # Update left child
                # (c + v)^2 = c^2 + 2*v*c + v^2
                sum2[2 * node] = (sum2[2 * node] + 2 * val * sum1[2 * node] + val * val * left_len) % MOD
                sum1[2 * node] = (sum1[2 * node] + val * left_len) % MOD
                lazy[2 * node] = (lazy[2 * node] + val) % MOD
                
                # Update right child
                sum2[2 * node + 1] = (sum2[2 * node + 1] + 2 * val * sum1[2 * node + 1] + val * val * right_len) % MOD
                sum1[2 * node + 1] = (sum1[2 * node + 1] + val * right_len) % MOD
                lazy[2 * node + 1] = (lazy[2 * node + 1] + val) % MOD
                
                lazy[node] = 0

        def update(node, l, r, ql, qr, val):
            if ql > r or qr < l:
                return
            if ql <= l and r <= qr:
                length = r - l + 1
                sum2[node] = (sum2[node] + 2 * val * sum1[node] + val * val * length) % MOD
                sum1[node] = (sum1[node] + val * length) % MOD
                lazy[node] = (lazy[node] + val) % MOD
                return
            
            push(node, l, r)
            mid = (l + r) // 2
            update(2 * node, l, mid, ql, qr, val)
            update(2 * node + 1, mid + 1, r, ql, qr, val)
            
            sum1[node] = (sum1[2 * node] + sum1[2 * node + 1]) % MOD
            sum2[node] = (sum2[2 * node] + sum2[2 * node + 1]) % MOD

        def query_sum2(node, l, r, ql, qr):
            if ql > r or qr < l:
                return 0
            if ql <= l and r <= qr:
                return sum2[node]
            
            push(node, l, r)
            mid = (l + r) // 2
            return (query_sum2(2 * node, l, mid, ql, qr) + query_sum2(2 * node + 1, mid + 1, r, ql, qr)) % MOD

        total_sum = 0
        for i, x in enumerate(nums):
            prev = last_seen.get(x, -1)
            update(1, 0, n - 1, prev + 1, i, 1)
            total_sum = (total_sum + query_sum2(1, 0, n - 1, 0, i)) % MOD
            last_seen[x] = i
            
        return total_sum