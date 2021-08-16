class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = collections.defaultdict(int)
        for num in nums:
            d[num] += 1

        answer = []
        for key, value in d.items():
            answer.append([key, value])

        answer.sort(key=lambda x: x[1])
        answer = answer[::-1]
        answer = list(map(lambda x: x[0], answer))

        return answer[:k]
