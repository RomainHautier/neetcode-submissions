class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        i, j = 0, len(numbers)-1

        for _ in range(len(numbers)):

            s = numbers[i]+numbers[j]
            print(s, target)
            if s == target:
                return [i+1, j+1]
            elif s < target:
                i += 1
            else:
                j -= 1
        