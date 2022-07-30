n = int(input())
a, b = map(int, input().split())
m = int(input())

jokbo = {}
for _ in range(m):
    parent, child = map(int, input().split())
    if parent in jokbo.keys():
        jokbo[parent].append(child)
    else:
        jokbo[parent] = [child]


def compose_own_parents(me, jokbo):
    jokbo_keys = jokbo.keys()
    my_jokbo = [me]
    while True:
        find_parent = False
        for parent in jokbo_keys:
            if me in jokbo[parent]:
                find_parent = True
                my_jokbo.append(parent)
                me = parent
                break
        if not find_parent:
            break
    return my_jokbo


a_jokbo = compose_own_parents(a, jokbo)
b_jokbo = compose_own_parents(b, jokbo)

same_parent = None
from_a_to_same_parent = 0
for ix, a_parent in enumerate(a_jokbo):
    if a_parent in b_jokbo:
        same_parent = a_parent
        from_a_to_same_parent = ix
        break

if same_parent is None:
    print(-1)
else:
    chonsoo = b_jokbo.index(same_parent) + from_a_to_same_parent
    print(chonsoo)
