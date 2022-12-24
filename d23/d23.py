#!/usr/bin/python3

part2 = False
lines = open('i.txt', 'r').read().strip().split('\n')
e = set()
for i in range(len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j] == '#':
            e.add((j, i))

r = 0
order = [((-1, -1), (0, -1), (1, -1)), ((-1, 1), (0, 1), (1, 1)), ((-1, -1), (-1, 0), (-1, 1)), ((1, -1), (1, 0), (1, 1))]
while True:
    d = dict()
    pos = dict()
    for x, y in e:
        if set([(x + dx, y + dy) for dx in [-1, 0, 1] for dy in [-1, 0, 1] if not (dx == 0 and dy == 0)]).isdisjoint(e):
            continue

        for i in order:
            for dx, dy in i:
                if (x + dx, y + dy) in e:
                    break
            else:
                d[(x, y)] = (x + i[1][0], y + i[1][1])
                if (x + i[1][0], y + i[1][1]) not in pos:
                    pos[(x + i[1][0], y + i[1][1])] = 1
                else:
                    pos[(x + i[1][0], y + i[1][1])] += 1
                    
                break

    moved = False
    for (x, y), (nx, ny) in d.items():
        if pos[(nx, ny)] > 1:
            continue

        e.remove((x, y))
        e.add((nx, ny))
        moved = True

    if not part2 and r == 10:
        break

    if not moved and part2:
        break

    order = order[1:] + order[0:1]
    r += 1

sx = min(e, key=lambda x: x[0])[0]
ex = max(e, key=lambda x: x[0])[0]
sy = min(e, key=lambda x: x[1])[1]
ey = max(e, key=lambda x: x[1])[1]

if not part2:
    print((ey - sy + 1) * (ex - sx + 1) - len(e))
else:
    print(r + 1)
