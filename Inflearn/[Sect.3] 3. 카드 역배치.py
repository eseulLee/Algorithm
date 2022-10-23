import sys
sys.stdin = open('input.txt', 'rt')

arr = list(range(1, 21))

for _ in range(10):
    ai, bi = map(int, sys.stdin.readline().split())
    tmp = arr[ai-1:bi]
    arr[ai-1:bi] = tmp[::-1]

print(arr)