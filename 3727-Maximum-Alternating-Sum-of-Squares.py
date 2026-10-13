class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        squares = [x * x for x in nums]
        squares.sort(reverse=True)
        num_positive = (len(nums) + 1) // 2
        return sum(squares[:num_positive]) - sum(squares[num_positive:])