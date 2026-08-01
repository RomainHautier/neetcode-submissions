class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash = {num: None for num in nums}

        for num in nums:
            
            if hash[num] is not None:
                return True
            else:
                hash[num] = 1
        
        return False
