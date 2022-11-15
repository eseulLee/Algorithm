import sys
sys.stdin = open('../input.txt', 'rt')

L = int(input())
a = list(map(int, sys.stdin.readline().split()))
m = int(input())
# print(l,a,m,sep='\n')

a.sort()
for _ in range(m):
    a[-1] -= 1
    a[0] += 1
    a.sort()

res = a[-1] - a[0]
print(res)