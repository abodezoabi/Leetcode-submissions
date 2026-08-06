class Solution:
    def longestPalindrome(self, s: str) -> str:
        # classic 2-pointer approach  n^2
        # a more better approach is to start from two middles
        # 2 pinters starting from mid foreach i and expanding left,right

        ans = ""
        ans_len = 0
        for i in range(len(s)):
            # odd length palindrome
            r, l = i,i 
            while l>=0 and r<len(s) and s[l]==s[r]:
                if (r-l+1) > ans_len:
                    ans = s[l:r+1]
                    ans_len = r-l+1
                l-=1
                r+=1

            l,r = i,i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                if (r-l+1) > ans_len:
                    ans = s[l:r+1]
                    ans_len = r-l+1
                l-=1
                r+=1
        return ans


            # even length palindrome


        