class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counter = Counter(nums)
        int_list = []
        max_k = sorted(counter.values())[-k:]

        for num, kk in counter.items():
            # find the nums where the counter matches
            if kk in max_k:
                int_list.append(num)
                print(int_list)
            if len(int_list) == k:
                return int_list
            