import sys
sys.stdin = open('../input.txt', 'rt')

n = int(input())
a = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
m = int(input())

''' # case 01.
for i in range(m):
    x, y, z = map(int, sys.stdin.readline().split())
    tmp = [0] * n
    if y == 1:
        for i in range(n):
            tmp[(i+z)%n] = a[x-1][i]
    else:
        for i in range(n):
            tmp[(i-z)%n] = a[x-1][i]
    a[x - 1] = tmp

s, e, res = 0, n, 0
for i in range(n):
    for j in range(s, e):
        res += a[i][j]
    if i < n//2:
        s += 1
        e -= 1
    else:
        s -= 1
        e += 1
print(res)'''

# case 02.
for i in range(m):
    h, t, k = map(int, input().split())
    if t == 0:
        for _ in range(k):
            a[h-1].append(a[h-1].pop(0))   # 제일 앞에꺼 꺼내서 뒤에 넣기
    else:
        for _ in range(k):
            a[h-1].insert(0, a[h-1].pop()) # 제일 뒤에꺼 꺼내서 앞에 넣기

res = 0
s = 0
e = n-1
for i in range(n):
    for j in range(s, e+1):
        res += a[i][j]
    if i < n//2 :
        s += 1
        e -= 1
    else:
        s -= 1
        e += 1
print(res)