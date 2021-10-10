class Solution:
    def hammingWeight(self, n: int) -> int:
        binary = format(n, 'b')
        return binary.count('1')