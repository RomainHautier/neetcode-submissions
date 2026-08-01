class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(t) != len(s):
            return False
        
        letters = {l: 0 for l in s}
        
        for i in range(len(s)):

            letters[s[i]] += 1

            try:
                letters[t[i]] += 1
            except KeyError:
                return False
        
        
        for v in letters.values():
            if v % 2 !=0:
                return False
        
        return True