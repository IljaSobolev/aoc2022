#!/usr/bin/python3

part2 = True
lines = open('i.txt', 'r').read().strip().split('\n')

w, h = 1000, 800
arr = [['.' for _ in range(w)] for _ in range(h)]
maxy = 0
for line in lines:
    path = line.split(' -> ')
    for i in range(len(path) - 1):
        x1, y1 = map(int, path[i].split(','))
        x2, y2 = map(int, path[i + 1].split(','))
        arr[y1][x1] = '#'
        arr[y2][x2] = '#'

        if max(y1, y2) > maxy:
            maxy = max(y1, y2)

        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2)):
                arr[y][x1] = '#'

        if y1 == y2:
            for x in range(min(x1, x2), max(x1, x2)):
                arr[y1][x] = '#'

if part2:
    for x in range(w):
        arr[maxy + 2][x] = '#'

i = 0
complete = False
while not complete:
    sx, sy = 500, 0
    moved = True
    while moved:
        if sx <= 0 or sx >= w - 1 or sy >= h - 1 and not part2:
            complete = True
            break

        if sy < h - 1 and arr[sy + 1][sx] != '#':
            sy += 1
        elif sy < h - 1 and sx > 0 and arr[sy + 1][sx - 1] != '#':
            sy += 1
            sx -= 1
        elif sx < w - 1 and sy < h - 1 and arr[sy + 1][sx + 1] != '#':
            sy += 1
            sx += 1
        else:
            moved = False

    arr[sy][sx] = '#'
    i += 1
    if part2 and sx == 500 and sy == 0:
        break

print(i - (1 if not part2 else 0))
