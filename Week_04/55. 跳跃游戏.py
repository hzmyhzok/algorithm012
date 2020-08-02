class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max = 0
        for i , j in enumerate(nums):
            if max >= i and i + j > max:
                max = i + j
        return max >= i