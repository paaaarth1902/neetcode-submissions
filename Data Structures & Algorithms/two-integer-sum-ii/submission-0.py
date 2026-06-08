class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Define 2 pointers p1 and p2
        # start with p1 = 0 and p2 = len(numbers) - 1
        # start checking up untill p2 > p1
        # compute numbers[p1] + numbers[p2] - return [p1, p2] if equals
        # if sum is greater - p2 -=1
        # If sum is lesser than target - p2 += 1


        n = len(numbers) - 1
        p1, p2 = 0, n

        while(p2 > p1):
            sum = numbers[p1] + numbers[p2]
            if sum > target:
                p2 -= 1
            elif sum < target:
                p1 += 1
            else:
                return [p1 + 1, p2 + 1]

        return []

