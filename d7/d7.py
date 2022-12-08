#!/usr/bin/python3

lines = open('i.txt', 'r').read().strip().split('\n')[::-1]
size_dict = dict()
for t, line in enumerate(lines):
    if line[0] != '$':
        path = ''
        c = 0
        for i in range(t, len(lines)):
            if lines[i].startswith('$ cd ..'):
                c += 1
            elif lines[i].startswith('$ cd'):
                if c > 0:
                    c -= 1
                else:
                    path += '/' + lines[i][5:]

        size = 0
        if line.startswith('dir'):
            size = size_dict['/' + line[4:] + path]
        else:
            size = int(line.split()[0])

        if path not in size_dict:
            size_dict[path] = 0

        size_dict[path] += size

sizes = sorted(size_dict.values())
s = 0
for i in sizes:
    if i <= 100000:
        s += i

print(s)

m = 30000000 - (70000000 - sizes[-1])

i = 0
while sizes[i] < m:
    i += 1

print(sizes[i])
