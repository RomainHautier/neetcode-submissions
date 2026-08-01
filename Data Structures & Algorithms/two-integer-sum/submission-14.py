class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        indices = {}

        for idx, num in enumerate(nums):
            indices[num] = idx
        
        for i, num in enumerate(nums): 
            diff = target - num

            if diff in nums and indices[diff] != i:
                return [i, indices[diff]]

            