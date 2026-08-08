class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sub = nums[0]
        curent_sum = 0

        for n in nums:
            if curent_sum < 0:
                curent_sum = 0
            curent_sum +=n
            max_sub = max(max_sub, curent_sum)
        
        return max_sub
        