class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k%n
        tmp = [0] * n # init list of zeros 
        # temp is needed because in prev method i overwrote on values
        # and not kept in a way that rotates them 
        for i in range(n):
            tmp[(i + k) % n] = nums[i]

        nums[:] = tmp
 
        