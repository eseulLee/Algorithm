import sys
sys.stdin = open('../input.txt', 'rt')

n, m = map(int, input().split())
a = list(map(int, input().split()))

'''
- 용량크기의 최소(lt)는 1, 최대(rt)는 곡의 총 재생시간
- res 값을 바꿔나가면서 이분탐색으로 최적값 찾기
'''
def Count(capacity):
    cnt = 1
    s = 0
    for x in a:
        if s + x > capacity:
            cnt += 1
            s = x
        else:
            s += x
    return cnt

maxx = max(a)   # 가장 긴 곡의 용량 보다는 커야 함!
lt = 1
rt = sum(a)
res = 0
while lt <= rt:
    mid = (lt + rt) // 2
    if mid >= maxx and Count(mid) <= m:
        res = mid
        rt = mid -1
    else:
        lt = mid +1
print(res)




'''# case 01. 시간이 너무 오래 걸림..
res = 2147000000
for i in range(1,n-2):
    for j in range(i+1, n-1):

        a1 = a[:i]
        a2 = a[i:j]
        a3 = a[j:]
        print('a :',a1, a2, a3)
        s1 = sum(a1)
        s2 = sum(a2)
        s3 = sum(a3)
        print('s :',s1, s2, s3)
        s = max(s1, s2, s3)
        if s < res :
            res = s
        print('s:   ', s)
        print('res: ', res)

print('ans : ', res)'''