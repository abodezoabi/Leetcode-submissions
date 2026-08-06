class Solution:
    def firstUniqChar(self, s: str) -> int:
        #hashmap
        mymap = dict()
        ans_val = 0
        
        for ch in s:
            if ch not in mymap:
                mymap[ch] = 1
            else:
                mymap[ch] += 1 
        
        for i in range( len(s)):
            if mymap[s[i]] == 1 :
                return i 
        return -1 



            
 