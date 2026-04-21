class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        def divide(a, b):
            if b == 0:
                return sum_of_product

            # Determine if the result should be negative
            # Uses XOR operator: result is negative if signs differ
            negative = (a < 0) ^ (b < 0)

            # Work with absolute values
            dividend = abs(a)
            divisor = abs(b)

            quotient = 0
            while dividend >= divisor:
                dividend -= divisor
                quotient += 1
                
            return -quotient if negative else quotient
        sum_of_product =1
        ans = []
        arr= [1]*len(nums)
        i,j=0,0
        
        
        for i in range(len(nums)):
            for j in range(len(nums)):
                if j==i:
                    continue
                
                arr[i] *= nums[j]
        
            ans.append(arr[i])

        
        
        return ans
        
        


        