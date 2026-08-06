class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ## loop from left to right
        # maintain a sliding window 
        # one a repated char seen remove the most left char in the window 
        # each time track the max_len 

        charset = set()
        l,r = 0,0
        maxlen = 0 

        for r in range(len(s)):
            while s[r] in charset: # keep removing till not any dup in set then restart
                charset.remove(s[l])
                l+=1
            charset.add(s[r])
            maxlen = max(maxlen, r+1 -l)

        return maxlen

