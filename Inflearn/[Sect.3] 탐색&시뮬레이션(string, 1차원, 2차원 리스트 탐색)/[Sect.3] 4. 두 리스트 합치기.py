import sys
sys.stdin = open('../input.txt', 'rt')

''' # case 1.
tmp = []
for _ in range(2):
    n = int(input())
    lst = list(map(int, sys.stdin.readline().split()))
    tmp += lst
for i in sorted(tmp):
    print(i, end=' ')

> sort()의 시간복잡도 : nlogn >> 너무 오래 걸림!
> 이미 두개의 리스트 sort된 상태이므로 반복문으로 n 가능
'''

# case 2
n = int(input())
a = list(map(int, sys.stdin.readline().split()))
m = int(input())
b = list(map(int, sys.stdin.readline().split()))
p1 = p2 = 0
res = []
while (p1 < n) and (p2 < m) :
    if a[p1] <= b[p2] :
        res.append(a[p1])
        p1 += 1
    elif a[p1] > b[p2]:
        res.append(b[p2])
        p2 += 1
if p1 < n:
    res += a[p1:]
if p2 < n:
    res += b[p2:]
for x in res:
    print(x, end=' ')