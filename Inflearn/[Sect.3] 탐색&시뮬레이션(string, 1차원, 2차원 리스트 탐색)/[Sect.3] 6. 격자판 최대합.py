import sys
sys.stdin = open('../input.txt', 'rt')

# case 1 (answer)
n = int(input())
# 2차원 리스트 한번에 불러오기
a = [list(map(int, input().split())) for _ in range(n)]
largest = -2147000000
for i in range(n):
    sum1 = sum2 = 0
    for j in range(n):
        sum1 += a[i][j] # 가로
        sum2 += a[j][i] # 세로
    if sum1 > largest:
        largest = sum1
    if sum2 > largest:
        largest = sum2
sum1 = sum2 = 0
for i in range(n):
    sum1 += a[i][i]     # 우하향 대각선
    sum2 += a[i][n-i-1] # 우상향 대각선
if sum1 > largest:
    largest = sum1
if sum2 > largest:
    largest = sum2
print(largest)

''' # case 2 (self)
n = int(input())
arr = []
res = 0
for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))

for i in range(n):
    l1 = sum(arr[i])
    if res < l1:
        res = l1
    l2 = sum([arr[j][i] for j in range(n)])
    if res < l2:
        res = l2
c1=c2=0
for i in range(n):
    c1 += arr[i][i]
    c2 += arr[i][n-i-1]
res = max(c1, c2, res)
print(res)
'''