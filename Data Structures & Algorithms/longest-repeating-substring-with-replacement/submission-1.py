class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charCount = {}
        maxLen, maxFreq = 0, 0
        start = 0

        for end in range(len(s)):
            char = s[end]
            charCount[char] = charCount.get(char, 0) + 1
            maxFreq = max(maxFreq, charCount[char])
            if (end - start + 1) - maxFreq > k:
                charCount[s[start]] -= 1
                start += 1
            maxLen = max(maxLen, end - start + 1)
        
        return maxLen
