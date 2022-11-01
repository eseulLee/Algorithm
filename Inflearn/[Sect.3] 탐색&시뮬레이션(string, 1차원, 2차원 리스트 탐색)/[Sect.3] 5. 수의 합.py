import sys
sys.stdin = open('../input.txt', 'rt')

# case 1
# lt와 rt를 뒤로 하나씩 미뤄가면서 합을 구함
# m과 같거나 커지는 경우 합인 tot에서 시작값인 a[lt]를 빼주고 lt값을 +1 시켜줌
# rt가 n보다 크거나 같은 경우 break 로 while 문 종료

n, m = map(int, input().split())
a = list(map(int, input().split()))
lt = 0
rt = 1
tot = a[0]
cnt = 0
while True:
    if tot<m:
        if rt<n:
            tot += a[rt]
            rt += 1
        else:
            break
    elif tot == m:
        cnt += 1
        tot -= a[lt]
        lt += 1
    else:
        tot -= a[lt]
        lt += 1

print(cnt)

''' # case 2 > 시간 너무 오래 걸림 n^2
n, m = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
cnt = 0

for i in range(n):
   if a[i] == m:
       cnt += 1
   else :
       s = a[i]
       for j in range(i+1, n):
           s += a[j]
           if s == m:
               cnt += 1
print(cnt)
'''