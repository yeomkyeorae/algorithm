# tries = int(input())
#
# for t in range(1, tries + 1):
#     ingredient_num = int(input())
#
#     n = ingredient_num
#     arr = list(range(n)) + list(range(n))
#
#     print(arr)
#
#     ingredient_list = []
#     list_input = list(map(int, input().split()))
#
#     ingredient_list.append(list_input)
#
#     for i in range(1 << n):
#         for j in range(n):
#             if i & (1 << j):
#                 print(arr[j], end=", ")
#         print()
