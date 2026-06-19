class Solution:

    def penalty(self, stations, K, D):
        count = 0
        for i in range(len(stations) - 1):
            gap = stations[i + 1] - stations[i]
            count += math.ceil(gap / D) - 1
        return K >= count

    def minmaxGasDist(self, stations: List[int], k: int) -> float:

        l = 0
        h = max(stations[i + 1] - stations[i] for i in range(len(stations) - 1))

        while h - l > 1e-6:
            mid = (l + h) / 2

            if self.penalty(stations, k, mid):
                h = mid
            else:
                l = mid
        return l




        
        