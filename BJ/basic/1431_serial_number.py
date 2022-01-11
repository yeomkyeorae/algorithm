import sys
from functools import cmp_to_key

input = sys.stdin.readline


def getSum(string):
    summation = 0
    for ch in string:
        value = ord(ch)
        if 48 <= value <= 57:
            summation += int(ch)
    
    return [string, summation]


def compare(item1, item2):
    if item1[1] > item2[1]:
        return 1
    elif item1[1] < item2[1]:
        return -1
    else:
        if item1[0] > item2[0]:
            return 1
        else:
            return -1
    

N = int(input())

word_dict = dict()
word_len = set()
for _ in range(N):
    string = input().split('\n')[0]
    length = len(string)
    
    word_len.add(length)
    
    if word_dict.get(length):
        word_dict[length].append(getSum(string))
    else:
        word_dict[length] = [getSum(string)]
    
word_len = sorted(list(word_len))

for key in word_dict.keys():
    word_dict[key].sort(key=cmp_to_key(compare))
    
for key in word_len:
    for el in word_dict[key]:
        print(el[0])