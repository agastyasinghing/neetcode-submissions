class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        target = {}
        #how to assign s1 properly to target?
        for char in s1:
            target[char] = 1 + target.get(char, 0)
        window = {}
        left = 0
        
        for right in range(len(s2)):
            window[s2[right]] = 1 + window.get(s2[right], 0)
            if (right - left + 1) > len(s1):
                window[s2[left]] -= 1
                if window[s2[left]] == 0:
                    del window[s2[left]]
                left += 1
            if window == target:
                return True
            
        return False
        