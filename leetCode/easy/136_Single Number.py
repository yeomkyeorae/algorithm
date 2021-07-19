class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        num_dict = dict()

        for num in nums:
            if num_dict.get(num):
                del num_dict[num]
            else:
                num_dict[num] = True

        return list(num_dict.keys())[0]
