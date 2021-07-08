class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs = []
        for ch in s:
            if ch.isalnum():
                strs.append(ch.lower())

        answer = True
        for i in range(len(strs) // 2):
            if strs[i] != strs[len(strs) - 1 - i]:
                answer = False
                break

        return answer
