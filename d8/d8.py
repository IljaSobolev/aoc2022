#!/usr/bin/python3

a = open('i.txt', 'r').read().strip().split('\n')
h = len(a)
w = len(a[0])

v = [[0 for _ in range(w)] for _ in range(h)]

s = 0

for i in range(h):
    m = -1
    for j in range(w):
        height = int(a[i][j])
        if height > m:
            v[i][j] = 1
            m = height

for i in range(h):
    m = -1
    for j in range(w)[::-1]:
        height = int(a[i][j])
        if height > m:
            v[i][j] = 1
            s += 1
            m = height

for i in range(w):
    m = -1
    for j in range(h):
        height = int(a[j][i])
        if height > m:
            v[j][i] = 1
            s += 1
            m = height

for i in range(w):
    m = -1
    for j in range(h)[::-1]:
        height = int(a[j][i])
        if height > m:
            v[j][i] = 1
            s += 1
            m = height

def score(i, j):
    global a
    global w
    global h
    t = [0, 0, 0, 0]

    height = a[i][j]
    for d in range(i + 1, h):
        t[0] += 1
        if a[d][j] >= height:
            break

    for d in range(0, i)[::-1]:
        t[1] += 1
        if a[d][j] >= height:
            break

    for d in range(j + 1, w):
        t[2] += 1
        if a[i][d] >= height:
            break

    for d in range(0, j)[::-1]:
        t[3] += 1
        if a[i][d] >= height:
            break

    return t[0] * t[1] * t[2] * t[3]

s = sum([sum(i) for i in v])
print(s)

s = max([max([score(i, j) for j in range(w)]) for i in range(h)])
print(s)

