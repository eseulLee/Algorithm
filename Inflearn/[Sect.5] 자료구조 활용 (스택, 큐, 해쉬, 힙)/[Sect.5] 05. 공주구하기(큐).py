import sys
sys.stdin = open('../input.txt', 'rt')
from collections import deque

'''
QUEUE == FIFO (cf. STACK == LIFO)
- 먼저 들어간 게 먼저 나옴
- deque 사용
** DEQUE : 양쪽에서 모두 I/O 가능
- append, popleft 사용

문제접근
- 1~8까지 deque에 넣고 k번째마다 out(popleft)
- k번째가 아닌 경우, popleft하면서 append 동시 진행
- 1개가 될 때까지 진행

'''

n, k = map(int, input().split())
dq = list(range(1, n+1))
dq = deque(dq)
while dq:
    for _ in range(k-1):
        cur = dq.popleft()
        dq.append(cur)
    dq.popleft() # k번째 일 때 pop만 진행
    if len(dq) == 1:
        print(dq[0])
        dq.popleft() # break 대신 while문 종료를 위해 pop