class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Snapping rubber band problem 
        # we will consider the the string as charArray and put a rubber band at first char
        # we will start stretching it across till we encounter a duplicate element
        # Asa we encounter duplicate, we stop and check removing of which element from the stretched position will not break the expected outcome
        # we move the pointer to (that + 1) element and continue doing this
        # T.C -> O(n) as we traverse the array in single pass
        # S.C -> O(1) as we do not use extra memory


        # ------------------------"zxyzxyz"-------------------

        longestSubstr = 0
        ptr1 = 0
        ptr2 = 0
        charSet = set()

        for ptr2 in range(len(s)):
            while s[ptr2] in charSet:
                charSet.remove(s[ptr1])
                ptr1+=1

            charSet.add(s[ptr2])

            currLen = ptr2 - ptr1 + 1
            longestSubstr = max(longestSubstr, currLen)


        return longestSubstr