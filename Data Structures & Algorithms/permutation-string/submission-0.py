class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        s1_count = {}
        window_count = {}
        
        # Count characters in s1
        for c in s1:
            s1_count[c] = s1_count.get(c, 0) + 1
        
        # Initialize first window
        for i in range(len(s1)):
            window_count[s2[i]] = window_count.get(s2[i], 0) + 1
        
        # Check first window
        if s1_count == window_count:
            return True
        
        # Slide the window
        for i in range(len(s1), len(s2)):
            # Add new character
            new_char = s2[i]
            window_count[new_char] = window_count.get(new_char, 0) + 1
            
            # Remove old character
            old_char = s2[i - len(s1)]
            window_count[old_char] -= 1
            if window_count[old_char] == 0:
                del window_count[old_char]
            
            # Compare
            if s1_count == window_count:
                return True
        
        return False