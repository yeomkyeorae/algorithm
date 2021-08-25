class Solution:
    def __init__(self):
        self.total_answer = []
        self.target = 0
        self.candidates = []

    def go(self, num, comb, index):
        summation = sum(comb)
        if summation == self.target:
            self.total_answer.append(comb[:])
            return
        elif summation > self.target:
            return

        for ix, candidate in enumerate(self.candidates[index:]):
            comb.append(candidate)
            self.go(candidate, comb, ix + index)
            comb.pop()

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.candidates = candidates
        self.target = target

        self.go(0, [], 0)

        return self.total_answer
