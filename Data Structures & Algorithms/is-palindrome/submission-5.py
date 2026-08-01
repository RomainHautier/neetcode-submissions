class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        copy_s = ""
        leaned = re.sub(r"[^a-z0-9]", "", s.lower())
        print(leaned)

        for l in leaned[::-1]:
            
            copy_s += l
        
        print(copy_s)
        if copy_s == leaned:
            return True
        else:
            return False