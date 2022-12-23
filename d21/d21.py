#!/usr/bin/python3

part2 = False
lines = open('i.txt', 'r').read().strip().split('\n')
d = dict()

for line in lines:
    p = line.split(':')
    d[p[0]] = p[1]

def calc(c):
    expr_str = d[c].strip()
    if ' ' not in expr_str:
        return int(expr_str)

    a, _, b = expr_str.split()
    return eval(expr_str, {}, {a: calc(a), b: calc(b)})

def expr(c):
    expr_str = d[c].strip()
    if c == 'humn':
        return 'humn'

    if ' ' not in expr_str:
        return int(expr_str)

    a, o, b = expr_str.split()

    if c == 'root':
        return expr(a), expr(b)

    a, b = expr(a), expr(b)

    ah, bh = False, False
    if type(a) is int:
        ah = False
    elif a == 'humn':
        ah = True
    elif a[3]:
        ah = True

    if type(b) is int:
        bh = False
    elif b == 'humn':
        bh = True
    elif b[3]:
        bh = True

    return a, b, o, (ah or bh)

l, r = expr("root")
if 'humn' in r:
    l, r = r, l

def ev(r):
    if type(r) is int:
        return r

    if r[2] == '+':
        return ev(r[0]) + ev(r[1])
    if r[2] == '-':
        return ev(r[0]) - ev(r[1])
    if r[2] == '*':
        return ev(r[0]) * ev(r[1])
    if r[2] == '/':
        return ev(r[0]) / ev(r[1])

r = ev(r)

while l != 'humn':
    if l[2] == '+':
        if type(l[0]) is int or (l[0] != 'humn' and not l[0][3]):
            r = r - ev(l[0])
            l = l[1]
        else:
            r = r - ev(l[1])
            l = l[0]
    if l[2] == '-':
        if type(l[0]) is int or (l[0] != 'humn' and not l[0][3]):
            r = ev(l[0]) - r
            l = l[1]
        else:
            r = r + ev(l[1])
            l = l[0]
    if l[2] == '*':
        if type(l[0]) is int or (l[0] != 'humn' and not l[0][3]):
            r = r / ev(l[0])
            l = l[1]
        else:
            r = r / ev(l[1])
            l = l[0]
    if l[2] == '/':
        if type(l[0]) is int or (l[0] != 'humn' and not l[0][3]):
            r = r / ev(l[0])
            l = l[1]
        else:
            r = r * ev(l[1])
            l = l[0]
if part2:
    print(int(r))
else:
    print(int(calc('root')))
