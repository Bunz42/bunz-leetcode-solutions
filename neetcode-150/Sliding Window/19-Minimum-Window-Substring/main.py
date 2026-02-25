class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        freq_t = Counter(t)
        window = {}
        l = 0
        min_string = ""
        min_len = float('infinity')

        def is_valid():
            for char, count in freq_t.items():
                if window.get(char, 0) < count:
                    return False
            return True
        
        for r in range(len(s)):
            char = s[r]
            window[char] = window.get(char, 0) + 1

            while is_valid():
                if r - l + 1 < min_len:
                    min_string = s[l:r + 1]
                    min_len = r - l + 1

                l_char = s[l]
                window[l_char] -= 1
                l += 1
    
        return min_string  
