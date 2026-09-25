class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        import math

        left = 1
        right = max(piles)
        answer = max(piles)

        while left <= right:
            hours = 0
            k = (left + right) // 2
            for pile in piles:
                hours += int(math.ceil(pile / k))
            if hours <= h:
                answer = min(answer, k)
                right = k - 1
            if hours > h:
                left = k + 1
        return answer



        