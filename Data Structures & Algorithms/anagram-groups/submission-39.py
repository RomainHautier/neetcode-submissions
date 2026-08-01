class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        sorted_str = defaultdict(list)
        
        for s in strs:
            print("".join(sorted(s)))
            sorted_str["".join(sorted(s))].append(s)

        return list(sorted_str.values())
    
            


