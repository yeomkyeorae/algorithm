num = int(input())

member_dict = {}
age_set = set()
for _ in range(num):
    age, name = input().split()
    age = int(age)
    age_set.add(age)
    if age in member_dict.keys():
        member_dict[age].append(name)
    else:
        member_dict[age] = [name]

for one_age in sorted(list(age_set)):
    for one_name in member_dict[one_age]:
        print(one_age, one_name)
