#!/usr/bin/python3

lines = open('i.txt', 'r').read().strip().split('\n')

n = len(lines)
pairs = []
for line in lines:
    s = line.split()
    sx = int(s[2][2:-1])
    sy = int(s[3][2:-1])
    bx = int(s[8][2:-1])
    by = int(s[9][2:])

    pairs.append(((sx, sy), (bx, by)))

s = set()
for (sx, sy), (bx, by) in pairs:
    dist = abs(sx - bx) + abs(sy - by)

    x1 = sx - max(dist - abs(2000000 - sy), -1)
    x2 = sx + max(dist - abs(2000000 - sy), -1)
    s.update(range(x1, x2 + 1))
    
    if by == 2000000:
        s.remove(bx)

print(len(s))

for y in range(4000000 + 1):
    l = []
    for (sx, sy), (bx, by) in pairs:
        dist = abs(sx - bx) + abs(sy - by)

        x1 = sx - max(dist - abs(y - sy), -1)
        x2 = sx + max(dist - abs(y - sy), -1)
        if x1 <= x2:
            l.append((x1, x2 + 1))

    l.sort()
    maxx = l[0][1]
    for i in range(len(l) - 1):
        if l[i][1] > maxx:
            maxx = l[i][1]

        if l[i + 1][0] > maxx:
            ansx = l[i][1]
            ansy = y
            print(ansx * 4000000 + ansy)
            exit(1)
