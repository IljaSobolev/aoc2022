#!/usr/bin/python3

import math

entries = open('i.txt', 'r').read().strip().split('\n\n')

part2 = False

items = []
ops = []
test = []
counts = []

for i, entry in enumerate(entries):
    items.append([])
    lines = entry.split('\n')
    for w in lines[1].strip()[16:].split(', '):
        items[i].append(int(w))

    ops.append(lines[2].strip()[17:])
    divisor = int(lines[3].strip()[19:])
    true = int(lines[4].strip()[25:])
    false = int(lines[5].strip()[25:])
    test.append((divisor, true, false))
    counts.append(0)

lcm = math.lcm(test[0][0], test[1][0])
for i in range(2, len(test)):
    lcm = math.lcm(lcm, test[i][0])

for _ in range(10000 if part2 else 20):
    for s in range(len(items)):
        if not len(items[s]):
            continue

        op = ops[s]
        divisor, true, false = test[s]
        for i in range(len(items[s])):
            items[s][i] = eval(op, {}, {'old': items[s][i]})
            if not part2:
                items[s][i] //= 3
            if part2:
                items[s][i] %= lcm

            counts[s] += 1
            
            if items[s][i] % divisor == 0:
                items[true].append(items[s][i])
            else:
                items[false].append(items[s][i])

        items[s] = []

counts = sorted(counts)
print(counts[-1] * counts[-2])
