class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        # piles[i] = number of bananas in pile i
        # h number of hours you have to eat all bananas
        # decide banana per hour eating rate k
        #eahc hour choose a pile and eat k bananas
        # if piles[i] < k finish eating from there but not another
        # return min int such that you cna eat all bananas with h hours     
        # for each hours, the number of passes = piles[i] // k

        l = 1
        r = max(piles)
        min_speed = r
        
        while l <= r:
            mid = (l + r) // 2
            hours = 0
            for b in piles:
                if b % mid != 0:
                    rest = 1
                else:
                    rest = 0
                hours += b // mid + rest
            
            if hours > h: 
                l = mid + 1
            elif hours <= h:
                if mid < min_speed:
                    min_speed = mid
                r = mid - 1
        
        return min_speed
                
        


        