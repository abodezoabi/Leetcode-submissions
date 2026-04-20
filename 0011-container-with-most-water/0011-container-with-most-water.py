class Solution:
    def maxArea(self, height: List[int]) -> int:
        # O(n) solution using 2-Pointer
        ans=0
        right= len(height)-1
        left=0
        
        while left < right:
            area= (right-left) * min(height[left],height[right])
            ans= max(ans,area)
            left,right = (left+1, right) if height[left] < height[right] else (left, right-1)
            
        return ans



        