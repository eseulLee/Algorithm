import sys
sys.stdin = open('input.txt', 'rt')

N, M = map(int, input().split())
cnt = [0] * (N+M+3) #여유있게 만드려고 +3
max_ = -2147000000

for n in range(1, N+1):
    for m in range(1, M+1):
        cnt[n+m] += 1
for i in range(N+M+1):
    if cnt[i] > max_:
        max_ = cnt[i]
for i in range(N+M+1):
    if cnt[i] == max_:
        print(i, end=' ')