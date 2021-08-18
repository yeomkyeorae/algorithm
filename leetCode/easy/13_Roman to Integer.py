class Solution:
    def __init__(self):
        self.d = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        self.special_d = {
            'IV': 4,
            'IX': 9,
            'XL': 40,
            'XC': 90,
            'CD': 400,
            'CM': 900
        }

    def romanToInt(self, s: str) -> int:
        answer = 0

        has_special_d = True
        while has_special_d:
            tmp_has_special_d = False
            for special_symbol in self.special_d.keys():
                if special_symbol in s:
                    answer += self.special_d[special_symbol]
                    s = s.replace(special_symbol, '')
                    tmp_has_special_d = True
            if not tmp_has_special_d:
                has_special_d = False

        for symbol in s:
            answer += self.d[symbol]

        return answer
