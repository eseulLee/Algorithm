import sys
sys.stdin = open('../input.txt', 'rt')

n, c = map(int, input().split())
xi = [int(sys.stdin.readline()) for _ in range(n)]
xi.sort()

'''
- 거리의 최소는 1, 최대는 가장 큰 x좌표값
- 거리의 값이 mid보다 클 경우에 말 배치 가능
- 말끼리의 거리가 멀어야 하기 때문에 1에는 무조건 말이 있을 것이다
- 말이 1에 있다는 가정 하에 그 다음부터 mid보다 큰 거리면 말 배치
- 3마리 되면 res에 저장
'''
def Count(x):
    cnt = 1
    ep = xi[0]
    for i in xi[1:] :
        if i - ep >= x:
            cnt += 1
            ep = i
    return cnt

lt = 1
rt = xi[-1]
res = 0
while lt <= rt:
    mid = (lt+rt) //2
    if Count(mid) < c:
        rt = mid-1
    else:
        res = mid
        lt = mid+1
print(res)