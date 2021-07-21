class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        num_dict = {}
        for num in nums:
            try:
                num_dict[num] += 1
            except Exception:
                num_dict[num] = 1

        max_cnt = 0
        answer = 0
        for key in num_dict.keys():
            if num_dict[key] > max_cnt:
                max_cnt = num_dict[key]
                answer = key

        return answer
