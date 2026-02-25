class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_f = {}
        w_f = {}

        for i in range(len(s1)):
            s1_f[s1[i]] = s1_f.get(s1[i], 0) + 1
            w_f[s2[i]] = w_f.get(s2[i], 0) + 1

        if s1_f == w_f:
            return True

        l = 0
        for r in range(len(s1), len(s2)):
            w_f[s2[r]] = w_f.get(s2[r], 0) + 1
            
            w_f[s2[l]] -= 1
            if w_f[s2[l]] == 0:
                del w_f[s2[l]]
            
            l += 1

            if s1_f == w_f:
                return True
        
        return False

