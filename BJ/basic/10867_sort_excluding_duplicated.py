n = int(input())

num_set = set()
for input_num in input().split():
    num_set.add(int(input_num))
    
nums = list(num_set)
nums.sort()

print(' '.join(list(map(str, nums))))