import sys
sys.stdin = open('../input.txt', 'rt')

def digit_sum(x):
    sum = 0
    '''while x > 0:
        sum += (x % 10)
        x = x // 10
    return sum'''

    for i in str(x):
        sum += int(i)
    return sum

n = int(input())
a = list(map(int, input().split()))
max = -2147000000

for i in range(n):
    tot = digit_sum(a[i])
    if tot > max :
        max = tot
        res = a[i]

print(res)