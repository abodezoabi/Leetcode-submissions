class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hshmap = dict()
        for i in range(len(nums)):
            hshmap[nums[i]]=i

        for i in range(len(nums)):
            y = target - nums[i]

            if y in hshmap and hshmap[y] != i:
                return [i,hshmap[y]]
        