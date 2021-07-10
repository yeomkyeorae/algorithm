class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letters = []
        digits = []
        for log in logs:
            element = log.split(' ')[1]
            try:
                tmp = int(element)
                digits.append(log)
            except Exception:
                letters.append(log)

        letters.sort(key=lambda x: (
            ' '.join(x.split(' ')[1:]), x.split(' ')[0]))

        answer = []
        for l in letters:
            answer.append(l)
        for d in digits:
            answer.append(d)

        return answer
