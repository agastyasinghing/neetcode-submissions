class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        small = 0
        big = len(numbers) - 1 
        while small < big:
            currentSum = numbers[small] + numbers[big]
            if currentSum > target:
                big -= 1
            elif currentSum < target:
                small += 1
            else:
                return [small + 1, big + 1]

