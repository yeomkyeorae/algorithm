class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_list = [0] * 26
        t_list = [0] * 26

        for s_str in s:
            s_list[ord(s_str) - 97] += 1
        for t_str in t:
            t_list[ord(t_str) - 97] += 1

        for s_cnt, t_cnt in zip(s_list, t_list):
            if s_cnt != t_cnt:
                return False

        return True
