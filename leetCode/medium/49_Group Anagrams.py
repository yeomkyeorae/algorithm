class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = collections.defaultdict(list)
        for string in strs:
            sorted_ch_list = sorted(string)
            sorted_string = ''.join(sorted_ch_list)
            anagrams[sorted_string].append(string)

        answers = []
        for group in anagrams.values():
            answers.append(group)

        return answers
