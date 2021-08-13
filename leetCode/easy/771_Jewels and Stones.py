class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        d = collections.defaultdict(int)
        for s in stones:
            d[s] += 1
        cnt = 0
        for j in jewels:
            cnt += d[j]

        return cnt
