class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        stack = []
        cars = list(zip(position, speed))
        cars.sort(reverse=True)
        fleets = 0

        for pos, spd in cars:
            timetotarget = (target - pos)/spd

            if not stack:
                stack.append(timetotarget)
                fleets += 1
            elif stack:
                if timetotarget > stack[-1]:
                    stack.append(timetotarget)
                    fleets += 1
        
        return fleets

        