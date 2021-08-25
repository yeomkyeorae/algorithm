class Solution:
    def __init__(self):
        self.total_answer = []
        self.n = 0
        self.k = 0

    def go(self, start, answer):
        if len(answer) == self.k:
            self.total_answer.append(answer[:])
            return

        for num in range(start + 1, self.n + 1):
            answer.append(num)
            self.go(num, answer)
            answer.pop()

    def combine(self, n: int, k: int) -> List[List[int]]:
        self.n = n
        self.k = k

        self.go(0, [])

        return self.total_answer
