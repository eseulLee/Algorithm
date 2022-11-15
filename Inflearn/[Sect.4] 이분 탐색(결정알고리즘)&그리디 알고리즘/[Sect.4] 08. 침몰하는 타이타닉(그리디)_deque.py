import sys
sys.stdin = open('../input.txt', 'rt')
'''
# deque 사용해서 문제 풀어보기!
- list의 경우 원소들이 사라지면서 자리가 자꾸 이동됨
- deque 사용하면 pop되서 사라질 때 다음으로 자동으로 넘어감
- 맨앞, 맨뒤 모두 in/out 가능
'''
from collections import deque


n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
a = deque(a)
cnt = 0

while a:
    if len(a) == 1:
        cnt += 1
        break
    if a[0] + a[-1] > m:
        a.pop()      # 맨 뒷자리 pop
        cnt += 1
    else:
        a.popleft()  # 여기가 list와 차이점!
        a.pop()
        cnt += 1
print(cnt)