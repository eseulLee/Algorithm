import sys
sys.stdin = open('input.txt', 'rt')

n = int(input())
a = list(map(int, sys.stdin.readline().split()))
score = tot = 0

for i in range(n):
    if a[i] == 0:
        score = 0
    else:
        score += 1
        tot += score

print(tot)



