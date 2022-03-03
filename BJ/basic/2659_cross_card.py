clock_number_set = set()


def check_clock_number(str_lst):
    clock_number = int(''.join(str_lst))

    for _ in range(3):
        str_lst = [str_lst.pop()] + str_lst
        comp = int(''.join(str_lst))
        
        if clock_number > comp:
            clock_number = comp
    
    return clock_number
    

def make_all_clock_number(arr):
    global clock_number_set
    
    if len(arr) == 4:
        clock_number = check_clock_number(arr[:])
        clock_number_set.add(clock_number)
        return
    
    for i in range(1, 10):
        arr.append(str(i))
        make_all_clock_number(arr)
        arr.pop()


make_all_clock_number([])
clock_number_lst = list(clock_number_set)
clock_number_lst.sort()

input_str_lst = list(input().split(' '))
clock_number = check_clock_number(input_str_lst)

print(clock_number_lst.index(clock_number) + 1)