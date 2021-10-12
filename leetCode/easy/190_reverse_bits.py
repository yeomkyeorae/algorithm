class Solution:
    def reverseBits(self, n: int) -> int:
        reversed_binary = format(n, 'b')[::-1]
        remain = 32 - len(reversed_binary)
        for _ in range(remain):
            reversed_binary += '0'
        return int(reversed_binary, 2)
        