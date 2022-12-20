#!/usr/bin/python3

import sys
sys.setrecursionlimit(5000)

part2 = True
lines = open('i.txt', 'r').read().strip().split('\n')

coord = []
for line in lines:
    x, y, z = map(int, line.split(','))
    coord.append((x, y, z))

mx = max(x for x, y, z in coord) + 1
my = max(y for x, y, z in coord) + 1
mz = max(z for x, y, z in coord) + 1

volume = [[[0 for _ in range(mx)] for _ in range(my)] for _ in range(mz)]

for x, y, z in coord:
    volume[z][y][x] = 1

conn = set()

def dfs(u, vol, v, c):
    global conn

    x, y, z = u

    if v[z][y][x] != -1:
        return

    v[z][y][x] = c

    if x - 1 >= 0:
        if vol[z][y][x - 1] == 0:
            dfs((x - 1, y, z), vol, v, c)
    else: conn.add(c)
    if x + 1 < mx:
        if vol[z][y][x + 1] == 0:
            dfs((x + 1, y, z), vol, v, c)
    else: conn.add(c)
    if y - 1 >= 0:
        if vol[z][y - 1][x] == 0:
            dfs((x, y - 1, z), vol, v, c)
    else: conn.add(c)
    if y + 1 < my:
        if vol[z][y + 1][x] == 0:
            dfs((x, y + 1, z), vol, v, c)
    else: conn.add(c)
    if z - 1 >= 0:
        if vol[z - 1][y][x] == 0:
            dfs((x, y, z - 1), vol, v, c)
    else: conn.add(c)
    if z + 1 < mz:
        if vol[z + 1][y][x] == 0:
            dfs((x, y, z + 1), vol, v, c)
    else: conn.add(c)

v = [[[-1 for _ in range(mx)] for _ in range(my)] for _ in range(mz)]
c = 0
for z in range(mz):
    for y in range(my):
        for x in range(mx):
            if v[z][y][x] == -1 and volume[z][y][x] == 0:
                dfs((x, y, z), volume, v, c)
                c += 1

sa = 0
for x, y, z in coord:
    if x - 1 >= 0:
        if v[z][y][x - 1] in conn or not part2:
            sa += 1 - volume[z][y][x - 1]
    else: sa += 1
    if x + 1 < mx:
        if v[z][y][x + 1] in conn or not part2:
            sa += 1 - volume[z][y][x + 1]
    else: sa += 1
    if y - 1 >= 0:
        if v[z][y - 1][x] in conn or not part2:
            sa += 1 - volume[z][y - 1][x]
    else: sa += 1
    if y + 1 < my:
        if v[z][y + 1][x] in conn or not part2:
            sa += 1 - volume[z][y + 1][x]
    else: sa += 1
    if z - 1 >= 0:
        if v[z - 1][y][x] in conn or not part2:
            sa += 1 - volume[z - 1][y][x]
    else: sa += 1
    if z + 1 < mz:
        if v[z + 1][y][x] in conn or not part2:
            sa += 1 - volume[z + 1][y][x]
    else: sa += 1

print(sa)
