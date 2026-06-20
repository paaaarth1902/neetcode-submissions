class Solution:
    def findPeakElement(self, mountainArr: 'MountainArray', low: int, high: int) -> int:
        while low <= high:
            mid = low + (high - low) // 2

            if mid < mountainArr.length() - 1 and mountainArr.get(mid + 1) > mountainArr.get(mid):
                low = mid + 1
            
            elif mid > 0 and mountainArr.get(mid - 1) > mountainArr.get(mid):
                high = mid - 1
            
            else:
                return mid

    def binarySearch(self, mountainArr: 'MountainArray', target: int, low, high) -> int:
        while low <= high:
            mid = low + (high - low) // 2

            if mountainArr.get(mid) == target:
                return mid
            elif mountainArr.get(mid) < target:
                low = mid + 1
            else:
                high = mid - 1

        return -1
    
    def r_binarySearch(self, mountainArr: 'MountainArray', target: int, low, high) -> int:
        while low <= high:
            mid = low + (high - low) // 2

            if mountainArr.get(mid) == target:
                return mid
            elif mountainArr.get(mid) < target:
                high = mid - 1
            else:
                low = mid + 1

        return -1

    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:

        l = 0
        h = mountainArr.length() - 1

        peak = self.findPeakElement(mountainArr, l, h)

        o1 = self.binarySearch(mountainArr, target, l, peak)
        o2 = self.r_binarySearch(mountainArr, target, peak + 1, h)

        return o1 if o1 != -1 else o2