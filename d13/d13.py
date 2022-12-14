#!/usr/bin/python3

from functools import cmp_to_key

def parse(s):
    stack = []
    l = []
    for i in s.split(','):
        for _ in range(i.count('[')):
            l.append([])
            stack.append(l)
            l = l[-1]

        n = i.strip(',[]')
        if len(n):
            l.append(int(n))

        for _ in range(i.count(']')):
            l = stack.pop()
    
    return l[0]

def compare(a, b):
    if type(a) is int and type(b) is int:
        return b - a

    if type(a) is list and type(b) is list:
        for i, j in zip(a, b):
            c = compare(i, j)
            if c != 0:
                return c
                
        return len(b) - len(a)
    
    if type(a) is list and type(b) is int:
        return compare(a, [b])

    if type(a) is int and type(b) is list:
        return compare([a], b)
    
ind = []
lists = []
pairs = open('i.txt', 'r').read().strip().split('\n\n')

for i, p in enumerate(pairs):
    x, y = p.split('\n')
    l1 = parse(x)
    l2 = parse(y)
    lists += [l1, l2]
    if compare(l1, l2) > 0:
        ind.append(i + 1)

print(sum(ind))

lists += [[[2]], [[6]]]

lists.sort(key=cmp_to_key(compare), reverse=True)

i1 = lists.index([[2]]) + 1
i2 = lists.index([[6]]) + 1
print(i1 * i2)
