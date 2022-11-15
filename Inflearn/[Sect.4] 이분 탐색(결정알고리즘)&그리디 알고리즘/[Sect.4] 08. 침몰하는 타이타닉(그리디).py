import sys
sys.stdin = open('../input.txt', 'rt')

n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
cnt = 0

while a:
    if len(a) == 1:
        cnt += 1
        break
    if a[0] + a[-1] > m:
        a.pop() # 맨 뒷자리 pop
        cnt += 1
    else:
        a.pop(0)
        a.pop()
        cnt += 1
print(cnt)