N = int(input())

nums = list(map(int, input().split()))
nums.sort()

total = int(input())

if sum(nums) <= total:
    print(nums[-1])
else:
    flag = False
    for i in range(len(nums), -1, -1):
        before_sum = sum(nums[:i])
        current_after_sum = (len(nums) - i) * nums[i - 1]
        
        if total >= before_sum + current_after_sum:
            answer = nums[i - 1]
            
            checked = False
            while total >= before_sum + (len(nums) - i) * answer:
                checked = True
                answer += 1
            
            flag = True
            if checked:
                print(answer - 1)
            else:
                print(answer)
            break

    if not flag:
        print(total // len(nums))