class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if not nums: return -2
        if len(nums) == 1: return 0

        right_sum = sum(nums)
        left_sum = 0
        nums_len = len(nums)

        for i in range(0, nums_len):
            num = nums[i]
            right_sum -= num
            if right_sum == left_sum:
                return i
            left_sum += num
        
        return -1
