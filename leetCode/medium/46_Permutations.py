class Solution:
    def __init__(self):
        self.nums = []
        self.visited = []
        self.length = 0
        self.total_answer = []

    def go(self, before_ix, num, answer):
        if len(answer) == self.length:
            self.total_answer.append(answer[:])
            return

        for ix, num in enumerate(self.nums):
            if self.visited[ix] == 1:
                continue

            answer.append(num)
            self.visited[ix] = 1
            self.go(ix, num, answer)
            answer.pop()
            self.visited[ix] = 0

    def permute(self, nums: List[int]) -> List[List[int]]:
        self.nums = nums
        self.visited = [0] * len(nums)
        self.length = len(nums)

        for ix, num in enumerate(nums):
            answer = [num]
            self.visited[ix] = 1
            self.go(ix, num, answer)
            answer.pop()
            self.visited[ix] = 0

        return self.total_answer
