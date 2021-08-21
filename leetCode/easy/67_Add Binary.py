class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ten_a = int(a, 2)   # binary to int
        ten_b = int(b, 2)

        answer = format(ten_a + ten_b, "b")     # int to binary

        return answer
