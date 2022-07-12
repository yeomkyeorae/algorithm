import sys
from datetime import datetime

n = int(input())

min_value = sys.maxsize
min_name = ''
max_value = -sys.maxsize
max_name = ''
for _ in range(n):
    name, day, month, year = input().split(" ")
    day, month, year = int(day), int(month), int(year)

    seconds = datetime.strptime(
        "{}-{}-{}".format(year, month, day), "%Y-%m-%d").timestamp()

    if min_value > seconds:
        min_value = seconds
        min_name = name

    if max_value < seconds:
        max_value = seconds
        max_name = name

print(max_name)
print(min_name)
