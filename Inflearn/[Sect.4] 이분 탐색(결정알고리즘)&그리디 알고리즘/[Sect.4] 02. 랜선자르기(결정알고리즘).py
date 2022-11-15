import sys
sys.stdin = open('../input.txt', 'rt')

k, n = map(int, input().split())
'''
n개의 랜선의 길이는 1~k개의 랜선중 largest 사이
if, 1~1000 사이 일 때,
1. mid 500으로 잡고 계산해보기 > n보다 작아
2. 1~ mid(500) 의 mid 250으로 잡고 계산 > n보다 작아
3. 1~ mid(249) 의 mid 125로 잡고 계산 > 11개 가능!
3-1. res=125 로 일단 잡기
4. 최대 길이를 구해야 하므로 126 ~ 249 에서 찾아보기(mid 187) > 11개 가능!
4-1. res=187 로 갱신
5. 188~249 까지 다시 잡아서 계산 ...
'''
line = [int(sys.stdin.readline().strip()) for _ in range(k)]
sp = 1
ep = max(line)
res = []
while sp <= ep :
    mid = (sp+ep) //2
    lc = [i//mid for i in line]
    m = sum(lc)
    if m < n:
        ep = mid -1
    else:
        res.append(mid)
        sp = mid +1
print(max(res))

''' # case 02. 함수 정의 후 결정알고리즘
def Count(len):
    cnt=0
    for x in Line:
        cnt+=(x//len)
    return cnt

Line=[]
res=0
largest=0
for i in range(k):
    tmp=int(input())
    Line.append(tmp)
    largest=max(largest, tmp)
lt=1
rt=largest
while lt<=rt:
    mid=(lt+rt)//2
    if Count(mid)>=n:
        res=mid
        lt=mid+1
    else:
        rt=mid-1
print(res)'''