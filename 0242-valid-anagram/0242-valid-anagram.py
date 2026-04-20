from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Solution1 a simple function use

        if len(s) != len(t):
            return False 
        return Counter(s) == Counter(t)
        
        # more thought solution2 2-Hashmaps
        map1,map2 = {},{}

        for ch1 in s:
            map1[ch1] = map1.get(ch1, 0) + 1
        
        for ch2 in t:
            map2[ch2] = map2.get(ch2, 0) + 1

        for key in map1:
            if map1[key] != map2.get(key,0):
                return False
        return True


        