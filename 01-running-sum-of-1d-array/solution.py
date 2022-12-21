# URL: https://leetcode.com/problems/running-sum-of-1d-array/description

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        return self.opt_2(nums)

    def opt_1(self, nums: List[int]) -> List[int]:
        nums_length = len(nums)
        result = [0] * nums_length
        result[0] = nums[0]

        for i in range(1, nums_length):
            result[i] = result[i-1] + nums[i]
        
        return result

    def opt_2(self, nums: List[int]) -> List[int]:
        current_sum = 0
        result = []
        for n in nums:
            current_sum += n
            result.append(current_sum)

        return result
