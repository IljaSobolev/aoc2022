#!/usr/bin/python3

import queue

lines = open('i.txt', 'r').read().strip().split('\n')

m = [[ord(i) for i in l] for l in lines]
h = len(m)
w = len(m[0])

start = (0, 0)
end = (0, 0)

for i in range(h):
    for j in range(w):
        if m[i][j] == ord('S'):
            m[i][j] = ord('a')
            start = (j, i)
        if m[i][j] == ord('E'):
            m[i][j] = ord('z')
            end = (j, i)

g = [[[] for _ in range(w)] for _ in range(h)]

for i in range(h):
    for j in range(w):
        if j > 0 and m[i][j - 1] - m[i][j] >= -1:
            g[i][j].append((j - 1, i))
        if j < w - 1 and m[i][j + 1] - m[i][j] >= -1:
            g[i][j].append((j + 1, i))
        if i > 0 and m[i - 1][j] - m[i][j] >= -1:
            g[i][j].append((j, i - 1))
        if i < h - 1 and m[i + 1][j] - m[i][j] >= -1:
            g[i][j].append((j, i + 1))

dist = [[100000000 for _ in range(w)] for _ in range(h)]
dist[end[1]][end[0]] = 0
q = queue.PriorityQueue()
v = [[False for _ in range(w)] for _ in range(h)]

q.put((0, end))

while not q.empty():
    _, (x, y) = q.get()

    if v[y][x]:
        continue

    v[y][x] = True

    for adjx, adjy in g[y][x]:
        if dist[y][x] + 1 < dist[adjy][adjx]:
            dist[adjy][adjx] = dist[y][x] + 1
            q.put((dist[adjy][adjx], (adjx, adjy)))

print(dist[start[1]][start[0]])
print(min([min([dist[y][x] for x in range(w) if m[y][x] == ord('a')]) for y in range(h)]))
