class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        answer = ''
        for word in s.split(' '):
            if len(word) > 0:
                answer = word

        return len(answer)
