class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0 # O(1) space
        for i in range(len(nums)):  # O(n) time
            if nums[i] != val:
                nums[k] = nums[i]
                k+=1


        return k 
        