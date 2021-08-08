class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answers = [0] * len(temperatures)
        stack = []

        for today, t in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < t:
                day = stack.pop()
                answers[day] = today - day

            stack.append(today)

        return answers
