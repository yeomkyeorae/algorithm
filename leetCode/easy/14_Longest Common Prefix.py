class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pre_arr = []
        tmp_prefix = ''
        for ch in strs[0]:
            tmp_prefix += ch
            pre_arr.append(tmp_prefix)

        answer = ''
        for prefix in pre_arr:
            flag = True
            for word in strs:
                if prefix != word[:len(prefix)]:
                    flag = False
                    break

            if flag:
                answer = prefix
            else:
                break

        return answer
