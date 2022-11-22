import sys
sys.stdin = open('../input.txt', 'rt')
from collections import deque

n, m = map(int, input().split())
# Q = list(map(int, sys.stdin.readline().split()))
# dq = []
# for idx, val in enumerate(Q):
#     dq.append((idx, val))
Q = [(idx, val) for idx, val in enumerate(list(map(int, input().split())))]
Q = deque(Q)
res = 0
while True:
    cur = Q.popleft()
    if any(cur[1] < x[1] for x in Q): # 이미 pop한 상태이기 때문에 나머지 원소들과 비교하게 됨
        Q.append(cur)
    else:
        res += 1
        if cur[0] == m:
            print(res)
            break
