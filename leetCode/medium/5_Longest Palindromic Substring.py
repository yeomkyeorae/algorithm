class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2 or s == s[::-1]:
            return s

        if len(s) == 2:
            return s[0]

        length = 0
        answer = ''

        for i in range(len(s) - 1):
            left, right = i, i + 1
            tmp_answer = ''
            tmp_length = 0
            while left >= 0 and right < len(s):
                sub_string = s[left:right + 1]
                if sub_string[0] == sub_string[-1]:
                    tmp_answer = sub_string
                    tmp_length = len(sub_string)

                    if tmp_length > length:
                        length = tmp_length
                        answer = tmp_answer

                    left -= 1
                    right += 1
                else:
                    break

        for i in range(len(s) - 2):
            left, right = i, i + 2
            tmp_answer = ''
            tmp_length = 0
            while left >= 0 and right < len(s):
                sub_string = s[left:right + 1]
                if sub_string[0] == sub_string[-1]:
                    tmp_answer = sub_string
                    tmp_length = len(sub_string)

                    if tmp_length > length:
                        length = tmp_length
                        answer = tmp_answer

                    left -= 1
                    right += 1
                else:
                    break

        if answer == '':
            return s[0]

        return answer
