import sys


N = int(input())
C = int(input())

candidates = list(map(int, input().split(' ')))

pictures = []
candidate_dict = {}
for c in candidates:
    if len(pictures) < N:
        if not c in candidate_dict.keys():
            candidate_dict[c] = [1, 0]
        else:
            candidate_dict[c][0] += 1
        
        if not c in pictures:
            pictures.append(c)
        
        for key in pictures:
            candidate_dict[key][1] += 1
        
    else:                    
        if not c in pictures:
            if not c in candidate_dict.keys():
                candidate_dict[c] = [0, 0]
            candidate_dict[c][0] += 1
            
            del_key = 0
            candidate_cnt, candidate_age = sys.maxsize, -1
            for key in pictures:
                cnt, age = candidate_dict[key]
                
                if cnt < candidate_cnt:
                    candidate_cnt = cnt
                    candidate_age = age
                    del_key = key
                elif cnt == candidate_cnt and age > candidate_age:
                    candidate_age = age
                    del_key = key
                    
            ix = pictures.index(del_key)
            pictures[ix] = c
            candidate_dict[del_key] = [0, 0]
        else:
            candidate_dict[c][0] += 1

        for key in pictures:
            candidate_dict[key][1] += 1

        
pictures.sort()
print(' '.join(map(str, pictures)))