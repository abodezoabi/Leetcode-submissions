class Solution:
    def reverse(self, x: int) -> int:
        i=0
        summ=0
        sign = 1

        if x<0:
            sign = -1
            x= -1*x

        string = str(x)

        for ch in string:
            summ = summ + (int(ch)*(10**i))
            i+=1

        MIN_INT = -2**31
        MAX_INT = 2**31 - 1

        # After you calculate your 'result'
        if summ < MIN_INT or summ > MAX_INT:
            return 0
        
        return summ*sign
        

             


        