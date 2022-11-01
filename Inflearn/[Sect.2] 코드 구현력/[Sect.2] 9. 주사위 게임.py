import sys
sys.stdin = open('../input.txt', 'rt')

n = int(input())
res = -2147000000

for _ in range(n):
    a = list(map(int, sys.stdin.readline().split()))
    cnt = [0] * 7
    for i in a:
        cnt[i] += 1
    if 3 in cnt:
        res_ = 10000 + cnt.index(3) * 1000
    elif 2 in cnt:
        res_ = 1000 + cnt.index(2) * 100
    else:
        res_ = max(a) * 100
    if res_ > res:
        res = res_

print(res)

'''
n = int(input())
res = 0
for i in range(n):
    tmp = input().split()
    tmp.sort() # 정렬
    a, b, c = map(int, tmp)
    if a==b and b==c:
        money = 10000 + a*1000
    elif a==b or a==c:
        money = 1000 + (a*100)
    elif b==c:
        money = 1000 + (b*100)
    else:
        money = c*100
    if money > res:
        res = money
print(res)
'''