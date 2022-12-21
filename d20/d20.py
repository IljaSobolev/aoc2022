#!/usr/bin/python3

part2 = True
arr = list(map(int, open('i.txt', 'r').read().strip().split('\n')))

if part2:
    arr = list(map(lambda x: x * 811589153, arr))

arr = list(zip(arr, range(len(arr))))

for _ in range(10 if part2 else 1):
    for i in range(len(arr)):
        ind = 0
        for j in range(len(arr)):
            if arr[j][1] == i:
                ind = j
                break

        p = arr[ind]
        arr.remove(p)
        newind = (ind + p[0]) % len(arr)
        if newind != ind:
            if newind == len(arr): newind = 0
            if newind == 0:        newind = len(arr)

        arr.insert(newind, p)

arr = list(map(lambda x: x[0], arr))
z = arr.index(0)
print(arr[(z + 1000) % len(arr)] + arr[(z + 2000) % len(arr)] + arr[(z + 3000) % len(arr)])
