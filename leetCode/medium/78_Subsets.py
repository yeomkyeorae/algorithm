class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer = []
        for length in range(len(nums) + 1):
            for el in map(list, itertools.combinations(nums, length)):
                answer.append(el)
            
        return answer
