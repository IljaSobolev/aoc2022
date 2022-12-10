#!/usr/bin/python3

lines = open('i.txt', 'r').read().strip().split('\n')

def solve(n):
    global lines
    
    v = set()
    r = [[0, 0] for _ in range(n)]
    l = {'U': (0, 1), 'D': (0, -1), 'R': (1, 0), 'L': (-1, 0)}

    v.add(tuple(r[-1]))

    for line in lines:
        d, steps = line.split()
        steps = int(steps)
        dx, dy = l[d]
        for _ in range(steps):
            r[0][0] += dx
            r[0][1] += dy
            for i in range(1, n):
                h = r[i - 1]
                t = r[i]
                x = h[0] - t[0]
                y = h[1] - t[1]
                if abs(x) > 1 or abs(y) > 1:
                    if abs(x) == 1 and abs(y) == 2:
                        t[1] = (t[1] + h[1]) // 2
                        t[0] = h[0]
                    elif abs(x) == 2 and abs(y) == 1:
                        t[0] = (t[0] + h[0]) // 2
                        t[1] = h[1]
                    elif (abs(x) == 2 and abs(y) == 2) or abs(x) == 0 or abs(y) == 0:
                        t[1] = (t[1] + h[1]) // 2
                        t[0] = (t[0] + h[0]) // 2

            v.add(tuple(r[-1]))

    return len(v)

print(solve(2))
print(solve(10))
