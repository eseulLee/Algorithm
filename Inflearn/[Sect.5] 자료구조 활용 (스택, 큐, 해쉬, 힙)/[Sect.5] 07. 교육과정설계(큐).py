import sys
sys.stdin = open('../input.txt', 'rt')
from collections import deque
need = input()
n = int(input())
for i in range(n):
    plan = input()
    dq = deque(need)
    for x in plan:
        if x in dq:
            if x != dq.popleft() :    # 필수과목 순서대로 비교
                print('#%d NO'%(i+1))
                break
    else:
        if len(dq) == 0:
            print('#%d YES'%(i+1))
        else:
            print('#%d NO' % (i + 1))

