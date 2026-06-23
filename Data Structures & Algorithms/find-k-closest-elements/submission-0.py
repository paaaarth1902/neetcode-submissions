class Solution:

    def find_insert(self, arr, t):
        l = 0
        h = len(arr) - 1

        while l <= h:
            m = l + (h - l) // 2

            if arr[m] < t:
                l = m + 1
            elif arr[m] > t:
                h = m - 1
            else:
                return m

        return l

    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # step 1: search for an insert positoin for x
        res = self.find_insert(arr, x)
        cnt = k
        sol = []
        j = res # moves ahead
        i = res - 1 # moves behind

        while cnt > 0 and i >= 0 and j < len(arr):
            if abs(x - arr[i]) > abs(x - arr[j]):
                sol.append(arr[j])
                j += 1
            # elif (k - arr[i]) > (k - arr[j]):
            #     sol.append(arr[j])
            #     j += 1
            else:
                sol.append(arr[i])
                i -= 1

            cnt -= 1

        while cnt > 0 and j <= len(arr) - 1:
            sol.append(arr[j])
            j += 1
            cnt -= 1
        while cnt > 0 and i >= 0:
            sol.append(arr[i])
            i -= 1
            cnt -= 1

        
        sol.sort()
        return sol

            

            

            


        