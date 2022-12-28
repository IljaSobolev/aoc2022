#!/usr/bin/python3

lines = open('i.txt', 'r').read().strip().split('\n')

ans = 0
for num in lines:
    s = 0
    for i, c in enumerate(num[::-1]):
        s += 5**i * {'2': 2, '1': 1, '0': 0, '-': -1, '=': -2}[c]

    ans += s

x = ''
s = 0
i = 0
while True:
    digit = ((ans % (5**(i + 1))) - s) // (5**i)

    if digit > 2:
        digit -= 5

    s += digit * (5**i)
    i += 1
    
    x += {2: '2', 1: '1', 0: '0', -1: '-', -2: '='}[digit]

    if s >= ans:
        break

print(x[::-1])
