class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_alpha = [0] * 26
        for ch in s:
            s_alpha[ord(ch) - 97] += 1

        t_alpha = [0] * 26
        for ch in t:
            t_alpha[ord(ch) - 97] += 1

        ix = 0
        for s_cnt, t_cnt in zip(s_alpha, t_alpha):
            if s_cnt != t_cnt:
                break
            else:
                ix += 1

        return chr(97 + ix)
