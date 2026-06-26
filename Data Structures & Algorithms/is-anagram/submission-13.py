class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        countsS, countsT = {}, {}

        for c in s:
            countsS[c] = countsS.get(c, 0) + 1
        
        for c in t:
            countsT[c] = countsT.get(c, 0) + 1
        
        

        return countsS == countsT

        