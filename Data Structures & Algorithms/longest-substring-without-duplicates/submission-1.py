class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        charecter_set = set()
        result = 0

        for right in range(len(s)):
            while s[right] in charecter_set:
                charecter_set.remove(s[left])
                left += 1

            charecter_set.add(s[right])

            result = max(result, right - left + 1)

        return result