class Solution:
    def __init__(self):
        self.phone = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        self.answer = []
        self.digits = []

    def go(self, comb, index):
        if len(self.digits) == 0:
            return

        if index == len(self.digits):
            self.answer.append(comb)
            return

        for ch in self.phone[self.digits[index]]:
            self.go(comb + ch, index + 1)

    def letterCombinations(self, digits: str) -> List[str]:
        self.digits = digits
        self.go('', 0)

        return self.answer
