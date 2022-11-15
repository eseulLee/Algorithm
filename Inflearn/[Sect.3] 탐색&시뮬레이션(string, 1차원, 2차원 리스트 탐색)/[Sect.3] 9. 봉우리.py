import sys
sys.stdin = open('../input.txt', 'rt')

n = int(input())
a = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

# 가장자리 0 setting
a.insert(0, [0] * (n+2))
a.append([0] * (n+2))
for i in range(1, n+1):
    a[i].insert(0, 0)
    a[i].append(0)

# 가장자리 제외 1~ n-1까지만 진행 (최대가 n-1 * n-1)
# for문으로 돌면서 상하좌우 비교 후 조건 만족시 res += 1

''' # case 01.
res = 0
for i in range(1, n+1):
    for j in range(1, n+1):
        if max(a[i][j-1],a[i-1][j],a[i+1][j],a[i][j+1],a[i][j]) == a[i][j]:
            print(i, j)
            res += 1
print(res)'''

# case 02. -- all 사용하기
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
res = 0
for i in range(1, n+1):
    for j in range(1, n+1):
        if all(a[i][j] > a[i+dx[k]][j+dy[k]] for k in range(4)) :
            res += 1
print(res)
