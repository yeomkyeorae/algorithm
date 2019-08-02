num_list = list(map(int, input().split()))
num_list.sort()

alpha = input()
alpha_dict = {'A': 0, 'B': 1, 'C': 2}
alpha_list = [ch for ch in alpha]

for ch in alpha_list:
    print(num_list[alpha_dict[ch]], end=' ')
