num = int(input())

word_dict = {}
max_len = 0
for _ in range(num):
    word = input()

    if max_len < len(word):
        max_len = len(word)

    if len(word) in word_dict.keys():
        word_dict[len(word)].add(word)
    else:
        word_dict[len(word)] = {word}

for i in range(1, max_len + 1):
    if word_dict.get(i):
        for one_word in sorted(list(word_dict.get(i))):
            print(one_word)
