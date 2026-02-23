class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        frequencies = {}
        l = 0
        max_freq = 0
        max_len = 0

        for r in range(len(s)):
            char_entering = s[r]
            frequencies[char_entering] = frequencies.get(char_entering, 0) + 1
            
            max_freq = max(max_freq, frequencies[char_entering])
            valid_window = (r - l + 1) - max_freq <= k

            if not valid_window:
                char_leaving = s[l]
                frequencies[char_leaving] -= 1
                l += 1
            
            max_len = max(max_len, r - l + 1)
        
        return max_len
