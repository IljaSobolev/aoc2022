#!/usr/bin/python3

lines = open('i.txt', 'r').read().strip().split('\n')

screen = [['.' for _ in range(40)] for _ in range(6)]

def draw(cycle):
    global screen
    global x

    cycle %= (40 * 6)
    sx = cycle % 40
    sy = cycle // 40
    screen[sy][sx] = '#' if abs(sx - x) <= 1 else '.'

cycle = 0
x = 1
next = 20
s = 0
for line in lines:
    newx = x
    if line[0] == 'n':
        draw(cycle)
        cycle += 1
    elif line[0] == 'a':
        draw(cycle)
        draw(cycle + 1)
        cycle += 2
        newx = x + int(line.split()[1])

    if cycle >= next:
        s += next * x
        next += 40

    x = newx

print(s)

print('\n'.join([''.join(screen[i]) for i in range(6)]))
