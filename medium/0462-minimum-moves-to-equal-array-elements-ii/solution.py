class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        nums.sort()
        moves = 0
        left, right = 0, len(nums) - 1
        
        while left < right:
            moves += nums[right] - nums[left]
            left += 1
            right -= 1
            
        return moves