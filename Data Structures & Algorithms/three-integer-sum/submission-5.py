class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        numsSorted = sorted(nums)
        sol = []
        for i in range(len(numsSorted)):
            if i > 0 and numsSorted[i] == numsSorted[i - 1]:
                continue
            left = i + 1
            right = len(numsSorted) - 1
            while left < right:
                t = numsSorted[i] * -1
                if numsSorted[left] + numsSorted[right] > t:
                    right -= 1
                elif numsSorted[left] + numsSorted[right] < t:
                    left += 1
                else:
                    sol.append([numsSorted[left], numsSorted[right], numsSorted[i]])
                    left += 1
                    right -= 1
                    while left < right and numsSorted[left] == numsSorted[left - 1]:
                        left += 1
        return sol


        