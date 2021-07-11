class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = re.sub(r'[^\w]', ' ', paragraph)

        words = {}
        for p in paragraph.split(' '):
            p = p.lower()
            if p in banned or p == '':
                continue
            if p in words.keys():
                words[p] += 1
            else:
                words[p] = 1

        counts = collections.Counter(words)
        answer = counts.most_common(1)[0][0]

        return answer
