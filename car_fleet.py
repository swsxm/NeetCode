from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car_stats = sorted(zip(position, speed), reverse=True)
        count = 0
        fleets = []

        for p, s in car_stats:
            time_to_target = (target - p) / s
            if not fleets or time_to_target > fleets[-1]:
                count += 1
                fleets.append(time_to_target)

        return count

Test = Solution()
print(Test.carFleet(target = 12, position = [10, 8, 0, 5, 3], speed = [2, 4, 1, 1, 3]))
