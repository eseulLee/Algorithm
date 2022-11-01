import sys
sys.stdin = open('../input.txt', 'rt')

arr = list(range(1, 21))

for _ in range(10):
    ai, bi = map(int, sys.stdin.readline().split())
    tmp = arr[ai-1:bi]
    arr[ai-1:bi] = tmp[::-1]

print(arr)

'''
a = list(range(21))
for _ in range(10):
    s, e = map(int, input().split())
    for i in range((e-s+1)//2):
        a[s+i], a[e-i] = a[e-i], a[s+i]  # swap (반 바퀴만)
a.pop(0) # 0번째 인덱스 삭제
for x in a:
    print(x, end=' ')
'''