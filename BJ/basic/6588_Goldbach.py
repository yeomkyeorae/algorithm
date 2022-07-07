from sys import stdin


def erasto(N):
    nums = [1] * (N + 1)
    for i in range(2, 1001):
        if nums[i]:
            for j in range(2 * i, N + 1, i):
                nums[j] = 0

    return nums


nums = erasto(1000000)

while True:
    num = int(stdin.readline())
    if num == 0:
        break

    flag = True
    for i in range(3, len(nums)):
        if nums[i] and nums[num - i]:
            print(num, "=", i, "+", num - i)
            flag = False
            break

    if flag:
        print("Goldbach's conjecture is wrong.")
