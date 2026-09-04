class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target = {}

        for char in t:
            target[char] = 1 + target.get(char, 0)
        
        window = {}
        left = 0
        have = 0
        need = len(target)
        bestLength = float("inf")
        bestLeft = 0
        bestRight = 0
        

        for right in range(len(s)):
            rightChar = s[right]
            window[rightChar] = 1 + window.get(rightChar, 0)
            if rightChar in target and window[rightChar] == target[rightChar]:
                have += 1
            
            while have == need:
                currentLength = right - left + 1
                if currentLength < bestLength:
                    bestLength = currentLength
                    bestRight = right
                    bestLeft = left
                leftChar = s[left]
                window[leftChar] -= 1
                if leftChar in target and window[leftChar] < target[leftChar]:
                    have -= 1
                left += 1
        if bestLength == float("inf"):
            return ""
        else:
            return s[bestLeft:bestRight + 1]

