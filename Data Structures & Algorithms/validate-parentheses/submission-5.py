class Solution:
    def isValid(self, s: str) -> bool:

        mapa = {
        "(":")",
        "[":"]",
        "{":"}"
     }

        mystack = []

        for ch in s:
            if ch in mapa:
                mystack.append(ch)
            else:
                if not mystack:
                    return False
                x= mystack.pop()
                if mapa[x] != ch:
                    return False
        return len(mystack)==0
            


        