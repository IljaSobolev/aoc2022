#!/usr/bin/python3

import queue

lines = open('i.txt', 'r').read().strip().split('\n')
lines = lines[1:-1]
for i in range(len(lines)):
    lines[i] = lines[i][1:-1]

w = len(lines[0])
h = len(lines)
t = 1000

def to_set(board):
    b = set()
    for y in range(len(board)):
        for x in range(len(board[y])):
            if board[y][x] != '.':
                b.add((x, y, board[y][x]))

    return b 

def sim(b):
    newset = set()
    for x, y, c in b:
        if c == '<':
            newset.add(((x - 1) % w, y, '<'))
        if c == '>':
            newset.add(((x + 1) % w, y, '>'))
        if c == '^':
            newset.add((x, (y - 1) % h, '^'))
        if c == 'v':
            newset.add((x, (y + 1) % h, 'v'))

    return newset

board_set = set((x, y) for x in range(w) for y in range(h))
def empty_coords(b):
    return board_set.difference(set(map(lambda x: (x[0], x[1]), b)))

sets = [to_set(lines)]
for i in range(t):
    sets.append(sim(sets[-1]))

sets = list(map(empty_coords, sets))

g = dict()

for ts in range(t - 1):
    c = sets[ts]
    n = sets[ts + 1]
    for x, y in c:
        newel = []
        if (x - 1, y) in n:
            newel.append((ts + 1, y, x - 1))
        if (x + 1, y) in n:
            newel.append((ts + 1, y, x + 1))
        if (x, y - 1) in n:
            newel.append((ts + 1, y - 1, x))
        if (x, y + 1) in n:
            newel.append((ts + 1, y + 1, x))
        if (x, y) in n:
            newel.append((ts + 1, y, x))

        if (ts, y, x) in g:
            g[(ts, y, x)].extend(newel)
        else:
            g[(ts, y, x)] = newel

def shortest(sp, ep, sts):
    dist = [[[100_000_000 for _ in range(w)] for _ in range(h)] for _ in range(t)]
    dist[sts][sp[1]][sp[0]] = 0
    q = queue.PriorityQueue()
    v = set()

    q.put((0, sts, sp[1], sp[0]))

    while not q.empty():
        _, ts, y, x = q.get()

        if (ts, y, x) in v:
            continue

        v.add((ts, y, x))

        if (ts, y, x) not in g:
            continue

        for adjts, adjy, adjx in g[(ts, y, x)]:
            if dist[ts][y][x] + 1 < dist[adjts][adjy][adjx]:
                dist[adjts][adjy][adjx] = dist[ts][y][x] + 1
                q.put((dist[adjts][adjy][adjx], adjts, adjy, adjx))

    return min(dist[tt][ep[1]][ep[0]] for tt in range(t))

i = 0
s = shortest((0, 0), (w - 1, h - 1), 0)
while s == 100_000_000:
    i += 1
    s = shortest((0, 0), (w - 1, h - 1), i)

s = s + i + 1
print(s)

i = 0
s1 = shortest((w - 1, h - 1), (0, 0), s + i)
while s1 == 100_000_000:
    i += 1
    s1 = shortest((w - 1, h - 1), (0, 0), s + i)

s = s + s1 + i + 1

i = 0
s1 = shortest((0, 0), (w - 1, h - 1), s + i)
while s1 == 100_000_000:
    i += 1
    s1 = shortest((0, 0), (w - 1, h - 1), s + i)

s = s + s1 + i + 1
print(s)
