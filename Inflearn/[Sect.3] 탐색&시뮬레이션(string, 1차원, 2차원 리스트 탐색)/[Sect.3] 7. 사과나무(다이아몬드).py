import sys
sys.stdin = open('../input.txt', 'rt')
'''5
        0,2
    1,1 1,2 1,3
2,0 2,1 2,2 2,3 2,4
    3,1 3,2 3,3
        4,2
3
    0,1
1,0 1,1 1,2
    2,0
    
1. 초기값 s=e= n//2로 세팅
2. 다음 줄로 넘어가면서 s -= 1, e += 1 
3. 중간 줄 넘어가면서 반대로 s += 1, e -= 1
'''
n = int(input())
a = [ list(map(int, sys.stdin.readline().split())) for _ in range(n)]
res = 0
s = e = n//2
for i in range(n):
    for j in range(s, e+1) :
        res += a[i][j]
    if i < n//2 :
        s -= 1
        e += 1
    else:
        s += 1
        e -= 1
print(res)