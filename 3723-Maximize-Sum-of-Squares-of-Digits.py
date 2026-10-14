class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum > num * 9:
            return ""
        
        res = []
        for _ in range(num):
            digit = min(9, sum)
            res.append(str(digit))
            sum -= digit
            
        return "".join(res)